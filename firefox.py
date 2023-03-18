#!/bin/python3
import sys
import xpaths
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from getpass import getpass
from func_timer import timecounter

# Starting webdriver // FireFox

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))

# Instagram Functions

def instagram():
	driver.get("https://www.instagram.com/")
	print(">>> Please Loging to Your Instagram Account!")
	
def instagram_hashtag_engagement():
    hashtag = input(">>> Select 1 Hashtag: #")
    limit = input(">> How many posts would you like to interact with: ")
    driver.get("https://www.instagram.com/explore/tags/" + hashtag)
    timecounter(20)
    driver.find_element(by=By.XPATH, value=xpaths.instagram_post).click()
    timecounter(20)
    driver.find_element(by=By.XPATH, value=xpaths.instagram_like).click()