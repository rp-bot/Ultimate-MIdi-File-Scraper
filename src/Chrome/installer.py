"""Installer has many purposes. it can install and handle WebDriver"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.common.exceptions as selenium_exceptions
import selenium.webdriver.chrome.options as selenium_options

def install_driver():
    """recommended: install WebDriver into a global variable"""
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
