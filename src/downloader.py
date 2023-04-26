from Chrome.installer import install_driver, By, ActionChains, Keys
import time
from tqdm import tqdm
from pprint import pprint

DRIVER = install_driver()


def get_song_details():
    genre_tab = DRIVER.find_element(By.XPATH, '//*[@id="mainContent"]/div[7]')
    genre_list = genre_tab.find_elements(By.TAG_NAME, "a")

    time.sleep(1)

    for genre in tqdm(genre_list, desc=f"scraping midi files from genres: "):
        link = genre.get_attribute("href")
        DRIVER.execute_script(f"window.open('{link}', '_blank');")
        # switch to the second tab
        DRIVER.switch_to.window(DRIVER.window_handles[1])
        # //*[@id="mainContent"]/div[2]/div/a[2]
        artists = DRIVER.find_elements(By.CLASS_NAME, "genre-band-container")
        for artist in range(2, len(artists)+2):
            pprint(artists[artist-2].text)
        time.sleep(60)

    DRIVER.implicitly_wait(30)


if __name__ == '__main__':
    DRIVER.get("https://freemidi.org/all")
    get_song_details()
