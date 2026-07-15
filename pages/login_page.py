from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    # Enter the username
    def enter_username(self, username):
        self.enter_text(self.USERNAME, username)

    # Enter the password
    def enter_password(self, password):
        self.enter_text(self.PASSWORD, password)

    # Click the login button
    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    # Perform user login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Retrieve the login error message
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    # Verify successful login
    def is_login_successful(self):
        return "inventory" in self.driver.current_url

    # Login using the standard user account
    def login_as_standard_user(self):
        self.login("standard_user", "secret_sauce")

    # Check whether the login page is displayed
    def is_login_page_displayed(self):
        return self.is_visible(self.LOGIN_BUTTON)
