import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.menu_page import MenuPage


@allure.feature("Application")
@allure.story("Reset App State")
@allure.title("Verify Reset App State clears the cart")
def test_reset_app_state(setup):

    login = LoginPage(setup)
    inventory = InventoryPage(setup)
    menu = MenuPage(setup)

    login.login_as_standard_user()

    products = inventory.get_random_products()

    inventory.add_products_to_cart(products)

    assert inventory.get_cart_badge_count() == 4

    menu.open_menu()

    menu.reset_app_state()

    assert inventory.is_cart_empty()