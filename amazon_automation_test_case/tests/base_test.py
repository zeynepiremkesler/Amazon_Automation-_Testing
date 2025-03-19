import unittest
from selenium import webdriver
from config.config import BROWSER, CHROME_OPTIONS, CHROME_DRIVER_SERVICE


class BaseTest(unittest.TestCase):
    def setUp(self):
        # Retrieves the browser from the config and operates accordingly
        if BROWSER:
            self.driver = webdriver.Chrome(service=CHROME_DRIVER_SERVICE, options=CHROME_OPTIONS)
        else:
            raise ValueError("Invalid browser!!! Please try a valid browser.")

        # Starts and configures the browser
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com.tr/")

    def tearDown(self):
        # Closes the browser
        if self.driver:
            self.driver.quit()
