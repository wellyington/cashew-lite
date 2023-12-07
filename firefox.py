#!/bin/python3
import sys
import xpath
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

# Open Instagram

def instagram():
	driver.get("https://www.instagram.com/")
	print(">>> Please Loging to Your Instagram Account!")

# Instagram Engagement Function by Hashtag
	
def InstagramHashtagEngagement():
    
    # Set variable counter to 0 : Will be used to count engagements!
    counter = 0

    # Collection Hastag
    hashtag = input(">>> Select 1 Hashtag: #")
    limit = input(">>> How many posts would you like to interact with: ")
    
    # Opening Felected hashtag
    driver.get("https://www.instagram.com/explore/tags/" + hashtag)
    actions = ActionChains(driver)
    timecounter(20)

    # Opening First Post From The Hashtag Page
    driver.find_element(by=By.XPATH, value=xpath.instagram_post).click()
    timecounter(5)

    # Interating Engagements 

    while counter != int(limit):

        # Liking post
        actions.send_keys('l').perform()

        timecounter(2)

        # Moving to The Next Post
        actions.send_keys(Keys.ARROW_RIGHT).perform()
        
        # Update Variable 'counter'
        counter = counter + 1

        print(f">>> Engaged: {counter}")

        timecounter(2)
    
    # Closing Active Post
    actions.send_keys(Keys.ESCAPE).perform()
    
    print(">>> Engagement Completed.")