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
    
    url = driver.current_url

    # Set variable counter to 0 : Will be used to count engagements!
    counter = 0

    # Collect Hastag
    hashtag = input(">>> Select 1 Hashtag: #")

    # Instagram has recently limited the Hashtag search on web browsers, displaying only 28 posts when you look up on a specifc Hashtag!
    # This function has been set to engage with 20 posts by default.
    limit = 20
    
    # Opening Felected hashtag
    driver.get("https://www.instagram.com/explore/tags/" + hashtag)
    actions = ActionChains(driver)
    timecounter(20)

    # Opening First Post From The Hashtag Page
    driver.find_element(by=By.XPATH, value=xpath.instagram_post).click()
    timecounter(5)

    # Interating Engagements 

    while counter != int(limit):

        # Capturing Picture's URL Address
        url = driver.current_url

        # Resolving & Capturing Username
        try:
            username = driver.find_element(by=By.XPATH, value=xpath.instagram_username1).text
        except:
            try:
                username = driver.find_element(by=By.XPATH, value=xpath.instagram_username2).text
            except:
                username = driver.find_element(by=By.XPATH, value=xpath.instagram_username3).text

        # Liking post
        try:

            # Check if a SVG element with arial-label='Unlike' is TRUE

            svg_element = driver.find_element(By.XPATH, "//*[name()='svg' and @aria-label='Unlike']")
            aria_label = svg_element.get_attribute("aria-label")
            print("--------------------------------------")

            if aria_label == "Unlike":
                print("POST LIKED - MOVE NEXT")
                print("--------------------------------------")
                
                # Moving to The Next Post
                actions.send_keys(Keys.ARROW_RIGHT).perform()

                # Update Variable 'counter'
                counter = counter + 1
                timecounter(2)
            
        except:
            print(url)
            print(username)
            print("--------------------------------------")
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