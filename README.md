# cashew-lite
 
 Instagram Scrapper and Engagement Automation

## firefox.py

The firefox.py script is a Python program designed to automate engagement on Instagram by interacting with posts under a specified hashtag. It utilizes the Selenium WebDriver with Firefox to navigate through Instagram, log in to an account, and engage with posts.

## Prerequisites

Before using the script, make sure you have the following installed:

* Python 3
* Selenium
* WebDriver Manager

You can install the necessary Python packages using the following command:

`pip install selenium webdriver_manager`

## Usage

1. Open the script in a text editor and ensure all the required libraries are installed.

2. Run the script using the following command:

   `python3` - To start Python CLI

   `import firefox` - To import firefox.py functions into the CLI

   `firefox.instagram()` - To open instagram.com

3. The script will prompt you to log in to your Instagram account.

   `firefox.InstagramHashtagEngagement()` - To call the engagement function (after instagram account is logged in)

4. After logging in, you will be asked to enter a hashtag and the number of posts you want to interact with.

5. The script will then navigate to the specified hashtag page, open the first post, and begin engaging with the posts by liking them.

6. The engagement process will continue until the specified number of posts is reached.

## Customization

You can modify the script to fit your needs. For example, you might want to change the engagement actions or add additional functionalities.

## Disclaimer

This script automates interactions on Instagram, which may violate Instagram's terms of service. Use this script responsibly, and be aware that automated actions on social media platforms may result in account restrictions or bans.

## Note

Ensure you have the latest versions of the required libraries and the GeckoDriver. If you encounter issues, check the official documentation for each library for troubleshooting and updates.

### Disclaimer: This script is for educational purposes only. Use it at your own risk.
