from Chrome.installer import install_driver, By, ActionChains, Keys
from pprint import pprint
import time
import sqlite3

DRIVER = install_driver()

conn = sqlite3.connect('data/db/UltimateMidi.sqlite3')


def retrieve_from_genres():
    c = conn.cursor()
    select_data = '''SELECT * FROM genres'''
    c.execute(select_data)
    rows = c.fetchall()
    c.close()
    conn.close()
    return rows


def add_artists_bands(genre):
    c = conn.cursor()

    create_table = '''CREATE TABLE IF NOT EXISTS artists_bands (ID INTEGER PRIMARY KEY,genre TEXT,url TEXT)'''
    c.execute(create_table)
    conn.commit()

    DRIVER.switch_to.window(DRIVER.window_handles[-1])
    artists = DRIVER.find_elements(By.CLASS_NAME, "genre-band-container")
    for artist in range(len(artists)+2):
        curr = artists[artist -
                       2].find_elements(By.TAG_NAME, "a")[2].get_attribute("href")
    time.sleep(60)


if __name__ == '__main__':
    genres = retrieve_from_genres()
    for genre in genres:
        DRIVER.execute_script(f"window.open('{genre[-1]}');")
        add_artists_bands(genre)

        # pprint(genre)
