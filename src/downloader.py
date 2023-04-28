from Chrome.installer import install_driver, By, ActionChains, Keys
import time
from tqdm import tqdm
from pprint import pprint

DRIVER = install_driver()


def get_genres():
    genres = []
    genre_tab = DRIVER.find_element(By.XPATH, '//*[@id="mainContent"]/div[7]')
    genre_list = genre_tab.find_elements(By.TAG_NAME, "a")

    time.sleep(1)

    for genre in genre_list:
        link = genre.get_attribute("href")
        genres.append({
            "genre": genre.text,
            "url": link
        })

    return genres

# DRIVER.execute_script(f"window.open('{link}', '_blank');")
# DRIVER.switch_to.window(DRIVER.window_handles[1])


# artists = DRIVER.find_elements(By.CLASS_NAME, "genre-band-container")
 # pprint(artists[artist-2].text)

if __name__ == '__main__':
    DRIVER.get("https://freemidi.org/all")
    x = get_genres()
    pprint(x)
