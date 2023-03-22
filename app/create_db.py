import json
import sqlite3
import sql_queries as q


def spell_connect(dbname='spell_data.sqlite3'):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    return conn, curs


def spell_execute(conn, curs, query, params=(), mode=1):
    if mode == 1:
        result = curs.execute(query, params).fetchall()
    else:
        result = curs.executemany(query, params).fetchall()
    conn.commit()
    return result


def create_sql():
    with open('spell_data.json', encoding='utf-8') as f:
        spells = json.load(f)
    conn, curs = spell_connect()
    spell_execute(conn, curs, q.DROP_SPELL_TABLE)
    spell_execute(conn, curs, q.MAKE_SPELL_TABLE)
    spell_execute(conn, curs, q.INSERT_SPELL, spells, mode=0)


if __name__ == '__main__':
    create_sql()
