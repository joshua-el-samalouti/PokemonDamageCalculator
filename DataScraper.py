import pokebase as pb
import sqlite3 as sql

# wip

con = sql.connect('../../Database/pokemon.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS pokemon (
                id INTEGER PRIMARY KEY,
                name TEXT,
                base_experience INTEGER,
                height INTEGER,
                is_default INTEGER,
                order INTEGER,
                weight INTEGER,
                
                );''')
