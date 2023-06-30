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

# Open Instagram

def instagram():
	driver.get("https://www.instagram.com/")
	print(">>> Please Loging to Your Instagram Account!")

# Instagram Engagement Function by Hashtag
	
def instagram_hashtag_engagement():
    
    # Set variable counter to 0 : Will be used to count engagements!
    counter = 0

    # Collection Hastag
    hashtag = input(">>> Select 1 Hashtag: #")
    limit = input(">>> How many posts would you like to interact with: ")
    
    # Opening Felected hashtag
    driver.get("https://www.instagram.com/explore/tags/" + hashtag)
    timecounter(20)

    # Opening First Post From The Hashtag Page
    driver.find_element(by=By.XPATH, value=xpaths.instagram_post).click()
    timecounter(10)

    # Interating Engagements 

    while counter != int(limit):

        # Liking post
        driver.find_element(by=By.XPATH, value=xpaths.instagram_like).click()

        timecounter(15)

        # Moving to The Next Post
        try: 
            # Button to Move to The Next Post (All Posts but not First)
            driver.find_element(by=By.XPATH, value=xpaths.instagram_next2).click()
        except:
            # Button to Move to The Second Post (First post Only)
            # This button will will be clicked only once during execution
            driver.find_element(by=By.XPATH, value=xpaths.instagram_next1).click()
        
        # Update Variable 'counter'
        counter = counter + 1

        print(f">>> Engaged: {counter}")

        timecounter(5)
    
    # Closing Active Post
    driver.find_element(by=By.XPATH, value=xpaths.instagram_close_post).click()
    
    print(">>> Engagement Completed.")