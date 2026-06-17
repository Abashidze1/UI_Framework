from utils.logger import logger
from utils.waits import (
    wait_for_element_clickable,
    wait_for_element_visible,
    wait_for_element_present
)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator):
        logger.info(f"Finding element: {locator}")
        return wait_for_element_present(self.driver, locator)

    def click(self, locator):
        logger.info(f"Clicking element: {locator}")
        element = wait_for_element_clickable(self.driver, locator)
        element.click()

    def type(self, locator, text):
        logger.info(f"Typing '{text}' into element: {locator}")
        element = wait_for_element_clickable(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        logger.info(f"Getting text from element: {locator}")
        element = wait_for_element_visible(self.driver, locator)
        return element.text

    def is_displayed(self, locator):
        try:
            element = wait_for_element_visible(self.driver, locator)
            return element.is_displayed()
        except Exception:
            return False

    def get_current_url(self):
        return self.driver.current_url