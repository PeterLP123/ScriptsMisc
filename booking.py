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
from selenium.webdriver.common.action_chains import ActionChains

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

pattern = re.compile(r"^.*[Ll][Ii][Nn][Kk][^SsEe]*$")

# Wait until the booking time
pause.until(datetime(2023, 3, 27, 21, 53, 0))
logging.info('Booking time reached')
found = False
while not found:
    driver.refresh()
    # Find the button which reads "Book Now"
    elements = driver.find_elements(By.TAG_NAME, "a")
    for element in elements:
        if pattern.match(element.text):
            element.click()
            logging.info('Clicked on Book Now')
            found = True
            break
    continue

driver.stop_client()
