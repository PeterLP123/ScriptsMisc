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
# Wait until the booking time
pause.until(datetime(2023, 3, 27, 12, 49, 0))
driver.refresh()
logging.info('Page refreshed')
# Find the link which contains the text "Booking Events"
driver.find_element(By.LINK_TEXT, "Booking Events").click()
logging.info('Clicked on Book Now')
time.sleep(5)
