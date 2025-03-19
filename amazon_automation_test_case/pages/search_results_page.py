from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from config.config import SEARCH_BRAND
from pages.locators_page import Locators


class SearchResultsPage(BasePage):
    # The class that manages the operations on the search results page.

    def __init__(self, driver):
        super().__init__(driver)

    def verify_open_page(self):
        # Confirms that when the search button is pressed, results are opened according to the desired brand
        try:
            page_element = self.wait_for_element(*Locators.OPEN_PAGE)
            assert page_element.is_displayed(), "Error: Page not opened or wrong page opened!"
            print(f"Opened page verified: {SEARCH_BRAND}")
        except Exception as e:
            print(f"Error: Page could not be verified! Actual URL: {self.driver.current_url}\nError: {e}")

    def go_to_second_page(self):
        # Goes to second page and verifies that it is fully loaded.
        self.accept_cookies()

        try:
            # clicks on the second page button
            second_page_button = self.wait_for_element(*Locators.SECOND_PAGE_BUTTON)
            self.click_element(*Locators.SECOND_PAGE_BUTTON)
            print("second page button clicked.")

            # verifies that the second page is fully opened
            self.wait.until(EC.presence_of_element_located((*Locators.SECOND_PAGE_ACTIVE,)))
            print("Second page fully loaded.")
        except Exception as e:
            print(f"Error: Failed transition to second page . Error: {e}")

    def select_third_product(self):
        # clicks on the third product and goes to the product page
        try:
            third_product = self.wait_for_element(*Locators.THIRD_PRODUCT)
            self.driver.execute_script("arguments[0].click();", third_product)  # Click with JS
            print("Clicked on the third product and went to the product page.")
        except Exception as e:
            print(f"Error: Third product could not be clicked. Error: {e}")
