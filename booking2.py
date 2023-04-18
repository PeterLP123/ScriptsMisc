import logging
import re
import time
import pause
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://www.maynoothuniversity.ie/student-residences/bookings')
logging.info('Chromedriver opened successfully')
# Maximise the window
driver.maximize_window()
# Click on the button which reads "Allow all cookies"
allow_cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
allow_cookies.click()
time.sleep(1)
current_url = driver.current_url
while current_url == "https://www.maynoothuniversity.ie/student-residences/bookings":
    pause.until(datetime(2023, 4, 18, 21, 20, 0, 5))
    driver.refresh()
    # Find the button which reads "Book Now"
    try:
        element = driver.find_element(By.PARTIAL_LINK_TEXT, "click")
        element.click()
        logging.info('Clicked on Booking Link')
        break
    except NoSuchElementException:
        current_url = driver.current_url
        continue

driver.stop_client()
