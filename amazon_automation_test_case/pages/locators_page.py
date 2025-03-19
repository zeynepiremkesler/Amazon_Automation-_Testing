from selenium.webdriver.common.by import By
from config.config import SEARCH_BRAND


class Locators(object):
    # home_page Locators
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")  # Search box
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")  # Search button

    # base_page Locators
    COOKIE_BUTTON = (By.ID, "sp-cc-accept")  # Cookie accept button

    # search_results_page Locators
    OPEN_PAGE = (By.XPATH, f"//span[@class='a-color-state a-text-bold' and contains(text(), '{SEARCH_BRAND}')]")
    SECOND_PAGE_BUTTON = (By.XPATH, "//a[contains(@aria-label, '2 sayfasına git')]")
    SECOND_PAGE_ACTIVE = (By.XPATH,"//span[contains(@class, 's-pagination-item s-pagination-selected') and text()='2']")  # Verifies that the second page is opened
    THIRD_PRODUCT = (By.XPATH, "(//div[@data-component-type='s-search-result'])[3]//a")  # Information of the 3rd product.

    # product_page Locators
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")  # Add to Cart Button
    CART_CONFIRMATION = (By.ID, "sw-atc-details-single-container")  # Add to Cart Confirmation
    PRODUCT_TITLE = (By.ID, "productTitle")

    # cart_page Locators
    DELETE_BUTTON = (By.XPATH, "//input[@value='Sil']")
    CART_COUNT = (By.ID, "nav-cart-count")  # Shows how many items are in the cart
    CART_PAGE = (By.ID, "nav-cart")  # Go to cart button
