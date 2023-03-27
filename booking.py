import logging
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

# Wait until the booking time
pause.until(datetime(2023, 3, 27, 21, 53, 0))
logging.info('Booking time reached')
while True:
    try:
        driver.refresh()
        # Find the button which reads "Book Now"
        book_now = driver.find_element(By.LINK_TEXT, "Continuing Students")
        book_now.click()
        logging.info('Clicked on Book Now')
        break
    except NoSuchElementException as e:
        logging.info('Booking not available yet')
# Refresh the page
# driver.refresh()
# logging.info('Page refreshed')
# Find the link which contains the text "Booking Events"
# booking_events = driver.find_element(By.LINK_TEXT, "Before You Book")
# booking_events.click()
# logging.info('Clicked on Book Now')
