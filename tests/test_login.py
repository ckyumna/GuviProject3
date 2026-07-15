import pytest

from pages.login_page import LoginPage
from pages.menu_page import MenuPage

from utilities.json_reader import JsonReader
from utilities.logger import get_logger
from utilities.screenshot import Screenshot
import allure


logger = get_logger(__name__)

users = JsonReader.read_json("data/users.json")

@allure.feature("Login")
@allure.story("Valid Login")
@allure.title("Verify login using all predefined users")

@pytest.mark.parametrize(
    "user",
    users,
    ids=[user["username"] for user in users]
)

def test_login_with_all_users(setup, user):

    driver = setup

    login = LoginPage(driver)
    menu = MenuPage(driver)

    try:

        with allure.step(f"Login using {user['username']}"):

            logger.info(f"Testing {user['username']}")

            login.login(user["username"], user["password"])

        if user["valid"]:

            with allure.step("Verify successful login"):

                assert login.is_login_successful()

                logger.info("Login Successful")

            with allure.step("Logout"):

                menu.open_menu()

                assert menu.is_logout_visible()

                menu.click_logout()

        else:

            with allure.step("Verify locked user error"):

                assert "Epic sadface" in login.get_error_message()

    except Exception as e:

        Screenshot.capture(driver, user["username"])

        logger.error(str(e))

        raise