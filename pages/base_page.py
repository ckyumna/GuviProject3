from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # Click on a web element
    def click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    # Enter text into an input field
    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    # Retrieve text from a web element
    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text

    # Check whether an element is visible
    def is_visible(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    # Retrieve multiple web elements
    def get_elements(self, locator):
        return self.wait.until(
            EC.presence_of_all_elements_located(locator)
        )

    # Retrieve a single web element
    def get_element(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )