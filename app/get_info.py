import requests
from bs4 import BeautifulSoup


def get_spell(page):
    pierogi = []
    stock = BeautifulSoup(page.content, 'html.parser')
    name = stock.find('div', {'class': 'page-title page-header'})
    info = stock.find(id='page-content')
    spinfo = info.find_all(['p', 'li'])
    pierogi.append(name.text)
    # TODO Fix issue with the <div class="collapsible-block"> exception from "Healing Elixir" Spell
    for spin in spinfo:
        pierogi.append(spin.text)
    pierogi.append('\n')
    return pierogi


def scrape():
    root = requests.get('http://dnd5e.wikidot.com/spells')

    soup = BeautifulSoup(root.content, 'html.parser')
    i = 0

    with open('spell_data.txt', 'w', encoding='utf-8') as hope:
        while i in range(10):
            chunk = soup.find(id=f'wiki-tab-0-{i}')
            options = chunk.find_all('td')
            for option in options:
                look = option.find('a')
                if look is not None and (look['href'] != "/spell:healing-elixir-ua"):
                    spell_page = requests.get(f"http://dnd5e.wikidot.com{look['href']}")
                    spell = get_spell(spell_page)
                    hope.writelines(spell)
            print(f'Finished scraping all Level {i} Spells!')
            i += 1


if __name__ == '__main__':
    scrape()
