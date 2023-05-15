import requests
from Chrome.installer import install_driver, By, ActionChains, Keys
import time

DRIVER = install_driver()
DRIVER.get("https://freemidi.org/getter-65")
button = DRIVER.find_element(
    By.XPATH, '/html/body/div[2]/div[8]/div[1]/div/div[1]/div[3]/a[1]')
button.click()
time.sleep(2)
