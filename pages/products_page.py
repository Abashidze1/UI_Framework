from pages.base_page import BasePage
from locators.products_locators import ProductsLocators
from utils.logger import logger


class ProductsPage(BasePage):

    URL = "https://www.saucedemo.com/inventory.html"

    def get_page_title(self):
        return self.get_text(ProductsLocators.PAGE_TITLE)

    def get_product_names(self):
        logger.info("Получаю список названий товаров")
        elements = self.driver.find_elements(*ProductsLocators.PRODUCT_NAMES)
        return [el.text for el in elements]

    def get_product_prices(self):
        logger.info("Получаю список цен товаров")
        elements = self.driver.find_elements(*ProductsLocators.PRODUCT_PRICES)
        return [el.text for el in elements]

    def get_products_count(self):
        items = self.driver.find_elements(*ProductsLocators.PRODUCT_ITEMS)
        return len(items)

    def add_first_product_to_cart(self):
        logger.info("Добавляю первый товар в корзину")
        self.click(ProductsLocators.ADD_TO_CART_BUTTON)

    def get_cart_badge_count(self):
        return self.get_text(ProductsLocators.CART_BADGE)

    def is_cart_badge_displayed(self):
        return self.is_displayed(ProductsLocators.CART_BADGE)

    def go_to_cart(self):
        logger.info("Перехожу в корзину")
        self.click(ProductsLocators.CART_ICON)

    def sort_products(self, option):
        logger.info(f"Сортирую товары по: {option}")
        from selenium.webdriver.support.ui import Select
        dropdown = self.find(ProductsLocators.SORT_DROPDOWN)
        select = Select(dropdown)
        select.select_by_value(option)