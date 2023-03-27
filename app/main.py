from get_info import scrape
from compile_info import reggy
from create_db import create_sql


def create_spell_database():
    scrape()
    print('Spell data collected.')
    reggy()
    print('Spell data compiled.')
    create_sql()
    print("Database file 'spell_data.sqlite3' created.")


if __name__ == '__main__':
    create_spell_database()
