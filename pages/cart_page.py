from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        super().__init__(driver)

    # Retrieve product names and prices from the cart
    def get_cart_products(self):

        items = self.get_elements(self.CART_ITEMS)

        cart_products = []

        for item in items:

            name = item.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            price = item.find_element(
                By.CLASS_NAME,
                "inventory_item_price"
            ).text

            cart_products.append({
                "name": name,
                "price": price
            })

        return cart_products