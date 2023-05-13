from Chrome.installer import install_driver, By, ActionChains, Keys
import time
import sqlite3
from pprint import pprint
import threading
import re

ARTIST_NAME_PATTERN = r'\((.*?)\)'
SONG_TITLE_PATTERN = r'(.*?)\s+\('


def get_genres():
    select_genres = '''SELECT * FROM genres'''
    freeMIDI_db_cursor.execute(select_genres)
    rows = freeMIDI_db_cursor.fetchall()
    return rows


def add_page_urls(data: list):
    insert_command = f'''INSERT OR IGNORE INTO page_urls (genre_name, page_number, page_urls) VALUES (?, ?, ?)'''
    freeMIDI_db_cursor.executemany(insert_command, data)
    freeMIDI_db_conn.commit()


def get_page_urls():

    pass


def get_urls_in_genres(genres: list):
    for genre in genres:
        select_command = f"""SELECT * FROM page_urls WHERE genre_name = '{genre[1]}'"""
        freeMIDI_db_cursor.execute(select_command)
        rows = freeMIDI_db_cursor.fetchall()
        links_data = []
        for row in rows:
            DRIVER.get(row[-1])
            ul = DRIVER.find_element(
                By.XPATH, '/html/body/div[1]/div[3]/div[1]/ul[1]')
            li_s = ul.find_elements(By.TAG_NAME, "li")

            for li in li_s:
                link = li.find_element(By.TAG_NAME, "a").get_attribute("href")
                artist_name = re.findall(ARTIST_NAME_PATTERN, li.text)[0]
                song_title = re.findall(SONG_TITLE_PATTERN, li.text)[0]
                print("done")
                time.sleep(60)


if __name__ == '__main__':
    DRIVER = install_driver()
    #
    freeMIDI_db_conn = sqlite3.connect('data/db/midiworld_com.sqlite3')
    freeMIDI_db_cursor = freeMIDI_db_conn.cursor()
    #

    genres_list = get_genres()
    # get_urls_in_genres(genres_list)
    get_urls_in_genres(genres_list)

    #
    freeMIDI_db_cursor.close()
    freeMIDI_db_conn.close()
