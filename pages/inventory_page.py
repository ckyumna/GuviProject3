import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class InventoryPage(BasePage):

    CART_ICON = (By.ID, "shopping_cart_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    ADD_TO_CART_BUTTONS = (
        By.XPATH,
        "//button[text()='Add to cart']"
    )

    SORT_DROPDOWN = (
        By.CLASS_NAME,
        "product_sort_container"
    )
    PRODUCTS = (By.CLASS_NAME, "inventory_item")

    def __init__(self, driver):
        super().__init__(driver)

    # Check whether the cart icon is visible
    def is_cart_icon_visible(self):
        return self.is_visible(self.CART_ICON)

    # Retrieve all product names
    def get_product_names(self):
        products = self.get_elements(self.PRODUCT_NAMES)

        return [product.text for product in products]

    # Retrieve all product prices
    def get_product_prices(self):
        prices = self.get_elements(self.PRODUCT_PRICES)

        return [price.text for price in prices]

    # Retrieve complete product details
    def get_all_products(self):

        products = self.get_elements(self.PRODUCTS)

        product_list = []

        for product in products:
            name = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            price = product.find_element(
                By.CLASS_NAME,
                "inventory_item_price"
            ).text

            button = product.find_element(
                By.XPATH,
                ".//button"
            )

            product_list.append({
                "name": name,
                "price": price,
                "button": button
            })

        return product_list

    # Randomly select four products
    def get_random_products(self):

        products = self.get_all_products()

        return random.sample(products, 4)

    # Add selected products to the cart
    def add_products_to_cart(self, products):

        for product in products:
            product["button"].click()

    # Retrieve the cart badge count
    def get_cart_badge_count(self):
        return int(self.get_text(self.CART_BADGE))

    # Navigate to the shopping cart
    def open_cart(self):
        self.click(self.CART_ICON)

    # Select a sorting option from the dropdown
    def select_sort_option(self, option):
        dropdown = Select(
            self.get_element(self.SORT_DROPDOWN)
        )

        dropdown.select_by_visible_text(option)

    # Retrieve product prices as numeric values
    def get_product_price_values(self):
        prices = self.get_elements(self.PRODUCT_PRICES)

        return [
            float(price.text.replace("$", ""))
            for price in prices
        ]

    # Check whether the cart is empty
    def is_cart_empty(self):

        try:
            self.get_text(self.CART_BADGE)
            return False

        except TimeoutException:
            return True

