#!/bin/python3
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

def instagram_login():
	options = Options()
	options.headless = False
	driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
	driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
	print(">>> Please Loging to Your Instagram Account!")