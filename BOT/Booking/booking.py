from selenium import webdriver
import os
import Booking.constants as const
from selenium.webdriver.common.by import By

class Booking:
    def __init__(self, driver_path=r"C:\SeleniumDrivers\chromedriver-win64", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            print("Quitting the browser")
            self.driver.quit()

    def land_first_page(self):
        self.driver.get(const.BASE_URL)

    def close_signin_window(self):
        close_signin = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
        close_signin.click()

    def change_currency(self, currency=None):
        currency_element = self.driver.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()

        div = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="All currencies"]')
        btns = div.find_elements(By.CSS_SELECTOR, 'button')
        for btn in btns:
            text = btn.text.split("\n")
            if text[1] == currency:
                btn.click()
                break
        
        