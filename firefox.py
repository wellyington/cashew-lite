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
import sqlite3
from time import sleep
from getpass import getpass
import datetime
from func_timer import timecounter

import random
rSec = random.randint(5, 20)

# Create a SQLite database connection
conn = sqlite3.connect('cashew.db')
cursor = conn.cursor()

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

    # Create the emails table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS InstagramHashtagEngagement (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        handle TEXT,
        url TEXT,
        hashtag TEXT,
        date TEXT,
        time TEXT
    )
    ''')
    
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
    timecounter(rSec)

    # Opening First Post From The Hashtag Page
    driver.find_element(by=By.XPATH, value=xpath.instagram_post).click()
    timecounter(rSec)

    # Interating Engagements 

    while counter != int(limit):

        dateTime = datetime.datetime.now()
        dateNow = str(dateTime.date())
        timeNow = str(dateTime.strftime("%X"))

        # Capturing post's URL Address
        url = driver.current_url

        # Resolving & Capturing Username
        try:
            username = driver.find_element(by=By.XPATH, value=xpath.instagram_username1).text
        except:
            try:
                username = driver.find_element(by=By.XPATH, value=xpath.instagram_username2).text
            except:
                try:
                    username = driver.find_element(by=By.XPATH, value=xpath.instagram_username3).text
                except:
                    try:
                        username = driver.find_element(by=By.XPATH, value=xpath.instagram_username4).text
                    except:
                        try:
                            username = driver.find_element(by=By.XPATH, value=xpath.instagram_username5).text
                        except:
                            try:
                                username = driver.find_element(by=By.XPATH, value=xpath.instagram_username6).text
                            except:
                                username = driver.find_element(by=By.XPATH, value=xpath.instagram_username7).text

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
                timecounter(rSec)
            
        except:
            
            # Best POS for SQL execution HERE

            dataSet = (username, url, hashtag, dateNow, timeNow)
            cursor.execute("INSERT INTO InstagramHashtagEngagement (handle, url, hashtag, date, time) VALUES (?, ?, ?, ?, ?)", dataSet)
            conn.commit()
            print("Data Saved ---------------------------")
            print(f"Handle: {username}")
            print(f"Post's URL: {url}")
            print(f"Date: {dateNow} - Time {timeNow}")
            print("--------------------------------------")
            actions.send_keys('l').perform()

            timecounter(rSec)

            # Moving to The Next Post
            actions.send_keys(Keys.ARROW_RIGHT).perform()
            
            # Update Variable 'counter'
            counter = counter + 1

            print(f">>> Engaged: {counter}")

            timecounter(rSec)
    
    # Closing Active Post
    actions.send_keys(Keys.ESCAPE).perform()
    
    print(">>> Engagement Completed.")

def InstagramExploreEngagement():

    driver.get("https://www.instagram.com/explore/")
    actions = ActionChains(driver)
    timecounter(rSec)