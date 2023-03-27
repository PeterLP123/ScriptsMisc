import logging
import time
import pause
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.maynoothuniversity.ie/student-residences/bookings')
logging.info('Chromedriver opened successfully')
# Maximise the window
driver.maximize_window()
# Click on the button which reads "Allow all cookies"
allow_cookies = driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
allow_cookies.click()
time.sleep(1)
# Wait until the booking time
pause.until(datetime(2023, 3, 27, 12, 49, 0))
logging.info('Booking time reached')
# Refresh the page
driver.refresh()
logging.info('Page refreshed')
# Find the link which contains the text "Booking Events"
booking_events = driver.find_element(By.LINK_TEXT, "Before You Book")
booking_events.click()
logging.info('Clicked on Book Now')
time.sleep(500)
