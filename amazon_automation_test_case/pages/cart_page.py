from pages.base_page import BasePage
from pages.locators_page import Locators
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    # Class that manages cart operations

    def __init__(self, driver):
        super().__init__(driver)

    def delete_product(self):
        # Deletes the product in the cart and verifies its removal
        self.click_element(*Locators.DELETE_BUTTON)
        print("Products in the cart have been deleted.")

    def verify_cart_empty(self):
        # Verifies that the cart is empty
        cart_count_element = self.wait_for_element(*Locators.CART_COUNT)
        cart_count = cart_count_element.text.strip()

        assert cart_count == "0", f"Error: The cart is not empty! ({cart_count} There is a product)"
        print("The cart is empty.")
        return True
