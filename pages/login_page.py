from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.logger import logger


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com"

    def open(self):
        logger.info("Открываю страницу логина")
        super().open(self.URL)

    def login(self, username, password):
        logger.info(f"Логинюсь под пользователем: {username}")
        self.type(LoginLocators.USERNAME_INPUT, username)
        self.type(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def is_error_displayed(self):
        return self.is_displayed(LoginLocators.ERROR_MESSAGE)