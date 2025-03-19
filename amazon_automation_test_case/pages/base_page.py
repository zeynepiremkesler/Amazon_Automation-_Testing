from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import BASE_URL
from pages.locators_page import Locators


class BasePage:
    # Class containing fundamental methods for all pages

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_base_url(self):
        # Opens the specified URL
        self.driver.get(BASE_URL)

    def wait_for_element(self, by, locator):
        # Waits for the specified element to load or become visible
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def click_element(self, by, locator):
        # Clicks the specified element safely
        element = self.wait_for_element(by, locator)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, by, locator, text):
        # Enters text into the specified field
        element = self.wait_for_element(by, locator)
        element.clear()  # Clears the field first
        element.send_keys(text)

    def accept_cookies(self):
        # Accepts cookies (If the cookie button is visible)
        try:
            cookie_buttons = self.driver.find_elements(*Locators.COOKIE_BUTTON)
            if cookie_buttons:
                cookie_buttons[0].click()
                print("Cookies accepted.")
            else:
                print("Cookie button not visible, continuing.")
        except Exception as e:
            print(f" An error occurred while checking the cookie button: {e}")

    def go_to_homepage(self):
        # Navigates to the homepage
        self.driver.get(BASE_URL)
        print("Returned to the homepage.")

    def go_to_cartpage(self):
        # Goes to the cart page
        self.click_element(*Locators.CART_PAGE)
        print("Navigated to the cart page.")
        self.wait_for_element(*Locators.CART_COUNT)
