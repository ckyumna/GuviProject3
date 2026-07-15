import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Products")
@allure.story("Sorting")
@allure.title("Verify sorting functionality")
def test_sorting(setup):

    login = LoginPage(setup)
    inventory = InventoryPage(setup)

    login.login_as_standard_user()

    # Price Low to High
    inventory.select_sort_option("Price (low to high)")

    prices = inventory.get_product_price_values()

    assert prices == sorted(prices)

    # Name Z to A
    inventory.select_sort_option("Name (Z to A)")

    names = inventory.get_product_names()

    assert names == sorted(names, reverse=True)