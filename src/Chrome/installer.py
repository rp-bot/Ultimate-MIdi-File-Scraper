"""Installer has many purposes. it can install and handle WebDriver"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as selenium_exceptions
import selenium.webdriver.chrome.options as selenium_options


def install_driver(headless=False):
    """recommended: install WebDriver into a global variable"""
    OPTIONS = Options()
    if headless:
        OPTIONS.add_argument('--headless')
        OPTIONS.add_argument('--disable-gpu')
    OPTIONS.add_argument(
        "--user-data-dir=./src/Chrome/preferences")
    OPTIONS.page_load_strategy = 'normal'
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=OPTIONS)
