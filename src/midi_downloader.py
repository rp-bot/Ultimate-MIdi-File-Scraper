from Chrome.installer import install_driver, By, ActionChains, Keys
from pprint import pprint
import time
import sqlite3

DRIVER = install_driver()

conn = sqlite3.connect('data/db/UltimateMidi.sqlite3')
c = conn.cursor()

STR_TABLE = str.maketrans({"-": "_", " ": "_"})


def create_genre_queries():
    select_genres = '''SELECT * FROM genres'''
    c.execute(select_genres)
    rows = c.fetchall()

    select_artists_commands = []
    for genre in rows:
        select_artists_commands.append(
            (genre[1], f'''SELECT * FROM {genre[1].translate(STR_TABLE)}'''))

    return select_artists_commands


def download_midi(genre_queries):
    for genre, query in genre_queries:
        c.execute(query)
        rows = c.fetchall()


if __name__ == '__main__':
    genre_queries = create_genre_queries()
    download_midi(genre_queries)
