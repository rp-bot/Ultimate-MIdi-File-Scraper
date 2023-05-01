from Chrome.installer import install_driver, By, ActionChains, Keys
from pprint import pprint
import time
import sqlite3

DRIVER = install_driver()

conn = sqlite3.connect('data/.db/UltimateMidi.sqlite3')


def retrieve_from_genres():
    c = conn.cursor()
    select_data = '''SELECT * FROM genres'''
    c.execute(select_data)
    rows = c.fetchall()
    c.close()
    conn.close()
    return rows


def add_artists_bands(genre):
    artists = DRIVER.find_elements(By.CLASS_NAME, "genre-band-container")


if __name__ == '__main__':
    genres = retrieve_from_genres()
    # DRIVER.get("about:blank")
    for genre in genres:
        DRIVER.execute_script(f"window.open('{genre[-1]}', '_blank');")
        add_artists_bands(genre)
        time.sleep(10)
        # pprint(genre)
