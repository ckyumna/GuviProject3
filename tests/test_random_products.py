import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from utilities.logger import get_logger
from utilities.screenshot import Screenshot


logger = get_logger(__name__)


@allure.feature("Products")
@allure.story("Random Product Selection")
@allure.title("Verify random selection of four products")


def test_random_product_selection(setup):

    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    try:

        with allure.step("Login as standard user"):
            login.login_as_standard_user()

        with allure.step("Randomly select four products"):

            selected_products = inventory.get_random_products()

            assert len(selected_products) == 4

        with allure.step("Display selected product details"):

            for product in selected_products:

                logger.info(
                    f"Product: {product['name']} | Price: {product['price']}"
                )

                print(
                    f"{product['name']} - {product['price']}"
                )

    except Exception as e:

        Screenshot.capture(driver, "random_products")

        logger.error(str(e))

        raise