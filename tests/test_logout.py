import allure

from pages.login_page import LoginPage
from pages.menu_page import MenuPage

from utilities.logger import get_logger
from utilities.screenshot import Screenshot


logger = get_logger(__name__)


@allure.feature("Logout")
@allure.story("User Logout")
@allure.title("Verify user can logout successfully")

# Verify user can logout successfully.
def test_logout(setup):

    driver = setup

    login = LoginPage(driver)
    menu = MenuPage(driver)

    try:

        with allure.step("Login as standard user"):
            login.login_as_standard_user()

        with allure.step("Verify logout option is visible"):
            menu.open_menu()
            assert menu.is_logout_visible()

        with allure.step("Logout from application"):
            menu.click_logout()

        with allure.step("Verify login page is displayed"):
            assert login.is_login_page_displayed()

        logger.info("Logout test passed.")

    except Exception as e:

        Screenshot.capture(driver, "logout_failure")

        logger.error(str(e))

        raise