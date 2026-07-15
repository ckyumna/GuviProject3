from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        super().__init__(driver)

    # Navigate to the checkout page
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    # Enter customer's first name
    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME, first_name)

    # Enter customer's last name
    def enter_last_name(self, last_name):
        self.enter_text(self.LAST_NAME, last_name)

    # Enter customer's postal code
    def enter_postal_code(self, postal_code):
        self.enter_text(self.POSTAL_CODE, postal_code)

    # Proceed to the order summary page
    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)

    # Complete the purchase
    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    # Retrieve the order confirmation message
    def get_confirmation_message(self):
        return self.get_text(self.COMPLETE_HEADER)