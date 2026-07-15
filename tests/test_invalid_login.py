import pytest
import allure

from pages.login_page import LoginPage

from utilities.json_reader import JsonReader
from utilities.logger import get_logger
from utilities.screenshot import Screenshot


logger = get_logger(__name__)

users = JsonReader.read_json("data/invalid_users.json")


@allure.feature("Login")
@allure.story("Invalid Login")
@allure.title("Verify login with invalid credentials")
@pytest.mark.parametrize(
    "user",
    users,
    ids=[f"{u['username'] or 'empty'}-{u['password'] or 'empty'}" for u in users]
)

# Verify login is rejected for invalid credentials.
def test_invalid_login(setup, user):

    driver = setup
    login = LoginPage(driver)

    try:

        with allure.step(
            f"Attempt login with username='{user['username']}'"
        ):
            login.login(user["username"], user["password"])

        with allure.step("Verify error message is displayed"):
            assert "Epic sadface" in login.get_error_message()

    except Exception as e:

        Screenshot.capture(driver, "invalid_login")

        logger.error(str(e))

        raise