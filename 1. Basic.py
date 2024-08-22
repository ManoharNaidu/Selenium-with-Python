import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

myEmail = "9515972954"
myPassword = "Manu@2711"

os.environ['PATH'] += r'C:\SeleniumDrivers\chromedriver-win64'
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")

email.send_keys(myEmail)
password.send_keys(myPassword)

login = driver.find_element(By.NAME, "login")
login.click()


friends = driver.find_element(By.XPATH, "//a[@data-tab-key='Find Friends']")
friends.click()

add_friend_buttons = driver.find_elements(By.XPATH, "//button[text()='Add friend']")
for button in add_friend_buttons:
    button.click()
    time.sleep(2)  # Wait a bit before sending the next request
