import pytest

from utilities.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def setup():

    driver = DriverFactory.get_driver()

    yield driver

    driver.quit()