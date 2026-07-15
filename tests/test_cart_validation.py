import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utilities.logger import get_logger
from utilities.screenshot import Screenshot


logger = get_logger(__name__)


@allure.feature("Cart")
@allure.story("Cart Validation")
@allure.title("Verify cart contains selected products")

# Verify successful login using valid user credentials.
def test_cart_validation(setup):

    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    try:

        with allure.step("Login"):
            login.login_as_standard_user()

        with allure.step("Select random products"):
            selected_products = inventory.get_random_products()

        with allure.step("Add products to cart"):
            inventory.add_products_to_cart(selected_products)

        with allure.step("Open cart"):
            inventory.open_cart()

        with allure.step("Fetch cart products"):
            cart_products = cart.get_cart_products()

        with allure.step("Verify product count"):
            assert len(cart_products) == len(selected_products)

        with allure.step("Verify product details"):

            expected = [
                {
                    "name": product["name"],
                    "price": product["price"]
                }
                for product in selected_products
            ]

            assert sorted(
                expected,
                key=lambda x: x["name"]
            ) == sorted(
                cart_products,
                key=lambda x: x["name"]
            )

            logger.info("Cart validation successful.")

    except Exception as e:

        Screenshot.capture(driver, "cart_validation")

        logger.error(str(e))

        raise