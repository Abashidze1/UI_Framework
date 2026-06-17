from selenium.webdriver.common.by import By


class CartLocators:
    PAGE_TITLE = (By.CLASS_NAME, "title")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    CHECKOUT_BUTTON = (By.ID, "checkout")

    REMOVE_BUTTON = (By.XPATH, "(//button[contains(@id, 'remove')])[1]")