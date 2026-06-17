from selenium.webdriver.common.by import By


class ProductsLocators:
    PAGE_TITLE = (By.CLASS_NAME, "title")

    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")

    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    ADD_TO_CART_BUTTON = (By.XPATH, "(//button[contains(@id, 'add-to-cart')])[1]")

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")