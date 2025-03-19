import unittest
from selenium import webdriver
from config.config import BASE_URL, BROWSER, SEARCH_BRAND, IMPLICIT_WAIT, CHROME_DRIVER_SERVICE, CHROME_OPTIONS
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.base_page import BasePage


class AmazonAddToCartTest(unittest.TestCase):

    def setUp(self):
        # Retrieves the browser from the config and operates accordingly
        if BROWSER:
            self.driver = webdriver.Chrome(service=CHROME_DRIVER_SERVICE, options=CHROME_OPTIONS)
        else:
            raise ValueError("Invalid browser!!! Please try a valid browser.")

        # Starts and configures the browser
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICIT_WAIT)
        self.driver.get(BASE_URL)

    def test_amazon_add_to_cart(self):

        home = HomePage(self.driver)
        search_results = SearchResultsPage(self.driver)
        product = ProductPage(self.driver)
        cart = CartPage(self.driver)
        base = BasePage(self.driver)

        base.accept_cookies()  # Accepts cookies
        home.verify_homepage()  # Verifies that the homepage is loaded
        home.search_product(SEARCH_BRAND)  # Searches for the desired brand
        search_results.verify_open_page()  # Verifies that the opened page belongs to the brand
        search_results.go_to_second_page()  # Navigates to the second page and verifies that it is the second page
        search_results.select_third_product()  # Navigates to the third product on the second page
        product.verify_product_page()  # Verifies that the user is on the third product's page from the top
        product.add_to_cart()  # Adds the product to the cart
        product.verify_product_added()  # Verifies that the product has been added to the cart

        # self.driver.get(BASE_URL + "gp/cart/view.html")
        base.go_to_cartpage()  # Navigates to the cart page
        cart.delete_product()  # Removes the product from the cart
        cart.verify_cart_empty()  # Verifies that the cart is empty
        base.go_to_homepage()  # Navigates to the homepage
        home.verify_homepage()  # Verifies that the user is on the homepage

    def tearDown(self):
        # Closes the browser after the test is completed
        self.driver.quit()
