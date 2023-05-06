from Chrome.installer import install_driver, By, ActionChains, Keys
import time
import sqlite3
from pprint import pprint
from songs_downloader import create_genre_queries
from lib import STR_TABLE


def get_genres():
    select_genres = '''SELECT * FROM genres'''
    url_db_cursor.execute(select_genres)
    rows = url_db_cursor.fetchall()
    return rows


def get_all_urls(genres):
    urls_dict = {}
    for genre in genres:
        fetch_urls = f'''SELECT * FROM {genre[1].translate(STR_TABLE)}_songs'''
        try:
            url_db_cursor.execute(fetch_urls)
            urls_list = url_db_cursor.fetchall()
            urls_dict.update({genre[1].translate(STR_TABLE): urls_list})
        except sqlite3.OperationalError:
            pprint(
                f'No table named: {genre[1].translate(STR_TABLE)}_songs, but the loop continued on')
            continue

    return urls_dict


def download_MIDI(urls_dict: dict, genre: str):
    # for all urls in the dictionary in the given
    pass


if __name__ == '__main__':

    url_db = sqlite3.connect('data/db/UltimateMidi.sqlite3')
    url_db_cursor = url_db.cursor()

    midi_db = sqlite3.connect('data/db/AllMIDI.sqlite3')
    midi_db_cursor = midi_db.cursor()

    # DRIVER = install_driver()

    genres = get_genres()

    all_urls_dict = get_all_urls(genres)

    download_MIDI(all_urls_dict, genres[0][1])

    url_db_cursor.close()
    url_db.close()

    midi_db_cursor.close()
    midi_db.close()
