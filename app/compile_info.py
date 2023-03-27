import json
import re


def reggy():
    with open('spell_data.txt', encoding='utf-8') as f:
        pages = f.readlines()

    class_patterns = "Artificer|Bard|Cleric|Druid|Paladin|Ranger|Sorcerer|Warlock|Wizard|\(Optional\)"
    lines = []
    big_list = []
    for page in pages:
        lines.append(page)
        if re.findall('({})(\n)'.format(class_patterns), page):
            spell = ''.join(lines)
            lines = []
            big_list.append(read_spell(spell))
    with open('spell_data.json', 'w', encoding='utf-8') as f:
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
        'Duration': "",
        'Concentration': False,
        'desc': "",
        'At Higher Levels': "",
        'Spell Lists': "",
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
        elif key == 'desc':
            next
        # take care of all directly mentioned tags,
        elif re.findall(key, spell):
            liz = re.split('({}\W)'.format(key), spell)
            liz = re.split('\n', liz[-1])
            # We need to use the duration and higher level tags to isolate the description
            # The easiest way to isolate the info we need is before the final split from the 'if source' statement
            if key == 'Duration':
                desc = re.findall('\B([A-Z].*)', ''.join(liz))
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
