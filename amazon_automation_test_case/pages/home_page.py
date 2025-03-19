from config.config import BASE_URL
from pages.base_page import BasePage
from pages.locators_page import Locators
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # Class containing operations for the Amazon homepage

    def __init__(self, driver):
        super().__init__(driver)

    def verify_homepage(self):
        # Verifies that we are on the Amazon homepage

        actual_url = self.driver.current_url

        assert BASE_URL in actual_url, f"Error: The homepage could not be verified. Expected: {BASE_URL}, Actual: {actual_url}"
        print("Home page successfully validated.")

    def search_product(self, product_name):
        # Search for the desired product
        self.enter_text(*Locators.SEARCH_BOX, product_name)
        self.click_element(*Locators.SEARCH_BUTTON)
