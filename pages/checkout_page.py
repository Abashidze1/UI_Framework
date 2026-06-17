from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from utils.logger import logger


class CheckoutPage(BasePage):

    def fill_customer_info(self, first_name, last_name, zip_code):
        logger.info(f"Заполняю форму: {first_name} {last_name}, {zip_code}")
        self.type(CheckoutLocators.FIRST_NAME_INPUT, first_name)
        self.type(CheckoutLocators.LAST_NAME_INPUT, last_name)
        self.type(CheckoutLocators.ZIP_CODE_INPUT, zip_code)

    def click_continue(self):
        logger.info("Нажимаю Continue")
        self.click(CheckoutLocators.CONTINUE_BUTTON)

    def click_finish(self):
        logger.info("Нажимаю Finish — подтверждаю заказ")
        self.click(CheckoutLocators.FINISH_BUTTON)

    def click_cancel(self):
        logger.info("Нажимаю Cancel")
        self.click(CheckoutLocators.CANCEL_BUTTON)

    def get_total_price(self):
        return self.get_text(CheckoutLocators.TOTAL_PRICE)

    def get_complete_header(self):
        return self.get_text(CheckoutLocators.COMPLETE_HEADER)

    def get_error_message(self):
        return self.get_text(CheckoutLocators.ERROR_MESSAGE)

    def is_error_displayed(self):
        return self.is_displayed(CheckoutLocators.ERROR_MESSAGE)

    def complete_checkout(self, first_name, last_name, zip_code):
        logger.info("Запускаю полный флоу оформления заказа")
        self.fill_customer_info(first_name, last_name, zip_code)
        self.click_continue()
        self.click_finish()