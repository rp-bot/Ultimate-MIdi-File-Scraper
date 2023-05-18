import __init__
import requests
from lib.db_ops import GetData
from Chrome.installer import install_driver, By, ActionChains, Keys
import time


def file_organizer(artist_name: str, song_name: str, genre: str):
    print(genre)


def download_all():
    all_midi = GetData(db="AllMIDI", table_name="dl_urls")
    all_midi_urls_list = all_midi.get_all()

    # loop through each url and download.
    for i, artist_i, artist_name, song_name, page_url, download_url, genre in all_midi_urls_list:
        DRIVER.get(page_url)
        time.sleep(2)
        button = DRIVER.find_element(
            By.XPATH, '/html/body/div[2]/div[8]/div[1]/div/div[1]/div[3]/a[1]')
        button.click()  # start download

        # file_organizer()


if __name__ == '__main__':
    DRIVER = install_driver(headless=False, download_mode=True)

    download_all()
