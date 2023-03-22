from get_info import scrape
from compile_info import reggy
from create_db import create_sql


def create_spell_database():
    # scrape()
    print('Spell data has been collected!')
    reggy()
    print('Spell data has been compiled!')
    create_sql()
    print("Look! We made an sql database!")


if __name__ == '__main__':
    create_spell_database()
