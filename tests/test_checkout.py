import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

from utilities.json_reader import JsonReader
from utilities.logger import get_logger
from utilities.screenshot import Screenshot


logger = get_logger(__name__)

data = JsonReader.read_json("data/checkout_data.json")


@allure.feature("Checkout")
@allure.story("Complete Checkout")
@allure.title("Verify successful checkout")
def test_checkout(setup):

    driver = setup

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    try:

        with allure.step("Login"):
            login.login_as_standard_user()

        with allure.step("Select products"):
            selected = inventory.get_random_products()

        with allure.step("Add products"):
            inventory.add_products_to_cart(selected)

        with allure.step("Open cart"):
            inventory.open_cart()

        with allure.step("Proceed to checkout"):
            checkout.click_checkout()

        with allure.step("Enter customer details"):

            checkout.enter_first_name(data["first_name"])
            checkout.enter_last_name(data["last_name"])
            checkout.enter_postal_code(data["postal_code"])

            checkout.continue_checkout()

        with allure.step("Capture order summary"):
            Screenshot.capture(driver, "order_summary")

        with allure.step("Finish order"):
            checkout.finish_order()

        with allure.step("Verify confirmation"):

            assert (
                checkout.get_confirmation_message()
                == "Thank you for your order!"
            )

            logger.info("Checkout completed successfully.")

    except Exception as e:

        Screenshot.capture(driver, "checkout_failure")

        logger.error(str(e))

        raise