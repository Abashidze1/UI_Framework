from pages.base_page import BasePage
from locators.cart_locators import CartLocators
from utils.logger import logger


class CartPage(BasePage):

    URL = "https://www.saucedemo.com/cart.html"

    def get_page_title(self):
        return self.get_text(CartLocators.PAGE_TITLE)

    def get_cart_items_count(self):
        items = self.driver.find_elements(*CartLocators.CART_ITEMS)
        return len(items)

    def get_item_names(self):
        logger.info("Получаю названия товаров в корзине")
        elements = self.driver.find_elements(*CartLocators.CART_ITEM_NAMES)
        return [el.text for el in elements]

    def get_item_prices(self):
        logger.info("Получаю цены товаров в корзине")
        elements = self.driver.find_elements(*CartLocators.CART_ITEM_PRICES)
        return [el.text for el in elements]

    def remove_first_item(self):
        logger.info("Удаляю первый товар из корзины")
        self.click(CartLocators.REMOVE_BUTTON)

    def click_continue_shopping(self):
        logger.info("Нажимаю Continue Shopping")
        self.click(CartLocators.CONTINUE_SHOPPING_BUTTON)

    def click_checkout(self):
        logger.info("Нажимаю Checkout")
        self.click(CartLocators.CHECKOUT_BUTTON)

    def is_empty(self):
        return self.get_cart_items_count() == 0