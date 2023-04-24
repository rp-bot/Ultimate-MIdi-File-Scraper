from Chrome.installer import install_driver, By,ActionChains, Keys
import time

DRIVER = install_driver()



def get_song_details():
    genre_tab = DRIVER.find_element(By.XPATH,'//*[@id="mainContent"]/div[7]')
    genre_list = genre_tab.find_elements(By.TAG_NAME, "a")

    time.sleep(1)
    
    for genre in genre_list:
        link = genre.get_attribute("href")
        
        DRIVER.execute_script(f"window.open('{link}', '_blank');")
        time.sleep(0.5)


if __name__ == '__main__':
    DRIVER.get("https://freemidi.org/all")
    get_song_details()