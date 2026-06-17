from selenium.webdriver.common.by import By


class CheckoutLocators:

    FIRST_NAME_INPUT = (By.ID, "first-name")

    LAST_NAME_INPUT = (By.ID, "last-name")

    ZIP_CODE_INPUT = (By.ID, "postal-code")

    CONTINUE_BUTTON = (By.ID, "continue")

    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    PAGE_TITLE = (By.CLASS_NAME, "title")

    TOTAL_PRICE = (By.CLASS_NAME, "summary_total_label")

    FINISH_BUTTON = (By.ID, "finish")

    CANCEL_BUTTON = (By.ID, "cancel")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")