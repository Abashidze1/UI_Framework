import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def driver():
    # открываем Safari перед каждым тестом
    driver = webdriver.Safari()
    driver.maximize_window()
    yield driver
    # закрываем браузер после каждого теста
    driver.quit()