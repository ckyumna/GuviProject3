import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Cart")
@allure.story("Cart Icon")
@allure.title("Verify shopping cart icon is visible after login")

# Verify that the shopping cart icon is displayed after a successful login.
def test_cart_icon_visible(setup):

    login = LoginPage(setup)
    inventory = InventoryPage(setup)

    with allure.step("Login as standard user"):
        login.login_as_standard_user()

    with allure.step("Verify cart icon is visible"):
        assert inventory.is_cart_icon_visible()