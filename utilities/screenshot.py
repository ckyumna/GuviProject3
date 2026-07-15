import os


class Screenshot:

    @staticmethod
    def capture(driver, filename):

        folder = "screenshots"

        os.makedirs(folder, exist_ok=True)

        driver.save_screenshot(
            os.path.join(folder, f"{filename}.png")
        )