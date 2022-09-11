from selenium import webdriver
<<<<<<< HEAD
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import options

options = options.Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-popup-blocking")
options.add_argument("--incognito")

keyword = 'Spongebob' #example

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://soapgate.org/')
   # Setup wait for later
wait = WebDriverWait(driver, 10)

    # Store the ID of the original window
original_window = driver.current_window_handle

    # Check we don't have other windows open already
assert len(driver.window_handles) == 1

time.sleep(5)
link = driver.find_element(By.CSS_SELECTOR, 'div.row:nth-child(1) > p:nth-child(2) > a:nth-child(1)')
link.click()


    # Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

    # Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break


time.sleep(5)
driver.switch_to.window()
go_button = driver.find_element(By.CSS_SELECTOR, '#btnhome')
go_button.click()
time.sleep(5)
search_box = driver.find_element(By.CSS_SELECTOR, '#txtSearch')
search_box.send_keys(keyword)
time.sleep(3)
enter_box = driver.find_element(By.CSS_SELECTOR, '#btnSearch')
enter_box.click()
=======
from webdriver_manager.chrome import ChromeDriverManager

>>>>>>> 51bcf6b0c0a71b0113e6afca7041e060d9d41ddc
