from pages.base_page import BasePage
from pages.locators_page import Locators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    # Class containing operations in product detail

    def __init__(self, driver):
        super().__init__(driver)

    def verify_product_page(self):
        # Verifies if it is on the product page
        product_title = self.wait_for_element(*Locators.PRODUCT_TITLE)
        assert product_title, f"Error: Product title not foun. URL: {self.driver.current_url}"
        print(f"Verified on the product page: {product_title}")

    def add_to_cart(self):
        # Adds product to cart
        self.click_element(*Locators.ADD_TO_CART_BUTTON)
        print("Product added to cart.")

    def verify_product_added(self):
        # Verifies that the product has been added to the cart
        confirmation_message = self.wait_for_element(*Locators.CART_CONFIRMATION)
        assert confirmation_message, "Error: Product could not be added to cart"
        print("Product successfully added to cart.")
