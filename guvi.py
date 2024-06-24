import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Path to the msedgedriver executable
EDGE_DRIVER_PATH = r'C:\Users\WELCOME\Downloads\edgedriver_win64\msedgedriver.exe'

# URL of the Instagram page
INSTAGRAM_URL = 'https://www.instagram.com/guviofficial/'

def initialize_driver():
    """
    Initialize the Microsoft Edge WebDriver.
    """
    edge_service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    edge_options = webdriver.EdgeOptions()
    return webdriver.Edge(service=edge_service, options=edge_options)

def print_cookies(driver, message):
    """
    Print the cookies stored in the browser.
    """
    cookies = driver.get_cookies()
    print(f"{message}:")
    for cookie in cookies:
        print(cookie)
    print("="*50)

def extract_followers_and_following(driver):
    """
    Extract the total number of followers and following from the Instagram page.
    """
    # Open the Instagram page
    driver.get(INSTAGRAM_URL)

    # Wait for the followers and following elements to be present
    try:
        followers_xpath = "//a[contains(@href,'followers')]/span"
        following_xpath = "//a[contains(@href,'following')]/span"

        followers_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, followers_xpath))
        )
        following_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, following_xpath))
        )

        # Extract the text content from the elements
        followers_count = followers_element.get_attribute('title')
        following_count = following_element.text

        return followers_count, following_count
    except TimeoutException:
        print("Failed to locate followers or following elements on the page.")
        return None, None

def main():
    """
    Main function to extract and display the total number of followers and following.
    """
    driver = initialize_driver()

    try:
        followers, following = extract_followers_and_following(driver)
        if followers is not None and following is not None:
            print(f"Followers: {followers}")
            print(f"Following: {following}")
        else:
            print("Unable to extract followers and following counts.")
    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()
