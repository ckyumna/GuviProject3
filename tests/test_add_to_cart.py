import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from utilities.logger import get_logger
from utilities.screenshot import Screenshot


logger = get_logger(__name__)


@allure.feature("Cart")
@allure.story("Add Products")
@allure.title("Verify selected products are added to cart")

# Verify that four randomly selected products are added to the shopping cart.
def test_add_products_to_cart(setup):

    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    try:

        with allure.step("Login as standard user"):
            login.login_as_standard_user()

        with allure.step("Randomly select four products"):
            selected_products = inventory.get_random_products()

            assert len(selected_products) == 4

        with allure.step("Add selected products to cart"):
            inventory.add_products_to_cart(selected_products)

        with allure.step("Verify cart badge count"):
            badge_count = inventory.get_cart_badge_count()

            logger.info(f"Cart Badge Count : {badge_count}")

            assert badge_count == 4

    # Capture a screenshot if the test fails
    except Exception as e:

        Screenshot.capture(driver, "add_to_cart")

        logger.error(str(e))

        raise