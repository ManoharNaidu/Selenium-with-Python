from selenium import webdriver
import os
import Booking.constants as const
import time

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers\chromedriver-win64", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            print("Quitting the browser")
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        self.maximize_window()