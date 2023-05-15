"""Installer has many purposes. it can install and handle WebDriver"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.chrome.options as selenium_options
import os

download_dir = os.path.abspath(
    '/Users/rpbot_mac/Documents/GitHub/UltimateMIdiChordParser/data')


def install_driver(headless=False):
    """recommended: install WebDriver into a global variable"""
    OPTIONS = Options()
    if headless:
        OPTIONS.add_argument('--headless')
        OPTIONS.add_argument('--disable-gpu')
    OPTIONS.add_argument(
        "--user-data-dir=./src/Chrome/preferences")
    OPTIONS.add_experimental_option('prefs', {
        'download.default_directory': download_dir,
        'download.prompt_for_download': True,
        'download.directory_upgrade': True,
        'safebrowsing.enabled': True
    })
    OPTIONS.page_load_strategy = 'normal'
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=OPTIONS)
