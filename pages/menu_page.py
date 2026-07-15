from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MenuPage(BasePage):

    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    RESET_APP_STATE = (By.ID, "reset_sidebar_link")

    def __init__(self, driver):
        super().__init__(driver)

    # Open the side navigation menu
    def open_menu(self):
        self.click(self.MENU_BUTTON)

    # Check whether the logout option is visible
    def is_logout_visible(self):
        return self.is_visible(self.LOGOUT_BUTTON)

    # Logout from the application
    def click_logout(self):
        self.click(self.LOGOUT_BUTTON)

    # Reset the application to its default state
    def reset_app_state(self):
        self.click(self.RESET_APP_STATE)