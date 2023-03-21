import json
import re


def reggy():
    with open('0spells.txt', encoding='utf-8') as f:
        pages = f.readlines()
        print(len(pages))

    class_patterns = "Artificer|Bard|Cleric|Druid|Paladin|Ranger|Sorcerer|Warlock|Wizard|\(Optional\)"
    lines = []
    big_list = []

    for page in pages:
        lines.append(page)
        if re.findall('({})(\n)'.format(class_patterns), page):
            # print(lines)
            spell = ''.join(lines)
            # print(spell)
            lines = []
            big_list.append(read_spell(spell))
            if big_list[-1] == 1:
                print(big_list[-2])
    print(len(big_list))
    with open('0spells.json', 'w', encoding='utf-8') as f:
        json.dump(big_list, f, indent=4)


def read_spell(spell):
    option = {
        'name': "",
        'Source': "",
        'spell_level': "Cantrip",
        'school': "",
        'ritual': False,
        'Casting Time': "",
        'Range': "",
        'Components': "",
        # 'materials': "",
        'Duration': "",
        'Concentration': False,
        'desc': "",
        'At Higher Levels': "",
        'Spell Lists': "",
        # 'archetype': "",
    }
    school_patterns = r"abjuration|conjuration|divination|enchantment|evocation|illusion|necromancy|transmutation"

    for key in option.keys():
        # four corners of tags that aren't named directly
        if key == 'school':
            student = re.findall(school_patterns, spell, re.IGNORECASE)
            option.update({key: student[0].capitalize()})
        elif key == 'name':
            name = re.split("\B([A-Z])", spell)
            option.update({key: name[0]})
        elif key == 'spell_level':
            level = re.findall("\B(\d..-level)", spell)
            if level:
                option.update({key: level[0]})
        # take care of all directly mentioned tags,
        elif re.findall(key, spell):
            liz = re.split('({}\W)'.format(key), spell)
            liz = re.split('\n', liz[-1])
            # this a bit hideous, but we need to use the duration and higher level tags to isolate the description
            # unfortunately that process only works if we do it before their final split from the next if statement
            if key == 'Duration':
                desc = re.findall('\B([A-Z].*)', ''.join(liz), flags=re.DOTALL)
                if re.findall('At Higher Levels', spell):
                    desc = re.split('At Higher Levels', desc[0])
                else:
                    desc = re.split('Spell Lists', desc[0])
                option.update({'desc': desc[0].strip()})
            # final split, isolate source from spell levels (including cantrip) and everyone else from word train stuff
            if key == 'Source':
                liz = re.split("\B([A-Z]|\d)", liz[0])
            else:
                liz = re.split("\B([A-Z]|\\.)", liz[0])
            option.update({key: liz[0].strip()})
            if (key == 'ritual') or (key == 'Concentration'):
                option.update({key: True})
    return option


if __name__ == '__main__':
    reggy()
