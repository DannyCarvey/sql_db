import requests
import re
from bs4 import BeautifulSoup


def get_spell(page):
    pierogi = []
    stock = BeautifulSoup(page.content, 'html.parser')
    name = stock.find('div', {'class': 'page-title page-header'})
    info = stock.find(id='page-content')
    spinfo = info.find_all(['p', 'li'])
    pierogi.append(name.text)
    for spin in spinfo:
        pierogi.append(spin.text)
    pierogi.append('\n')
    print(f'Spells Scraped: {q}')
    return pierogi


root = requests.get('http://dnd5e.wikidot.com/spells')

soup = BeautifulSoup(root.content, 'html.parser')
i = 0
q = 1

with open('0spells.txt', 'w', encoding='utf-8') as hope:
    while i in range(10):
        chunk = soup.find(id=f'wiki-tab-0-{i}')
        options = chunk.find_all('td')
        for option in options:
            look = option.find('a')
            if look is not None:
                spell_page = requests.get(f"http://dnd5e.wikidot.com{look['href']}")
                spell = get_spell(spell_page)
                q += 1
                hope.writelines(spell)
        i += 1
