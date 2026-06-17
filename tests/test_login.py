import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_successful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "secret_sauce")
    assert "inventory" in page.get_current_url()


@pytest.mark.negative
def test_login_with_wrong_password(driver):
    page = LoginPage(driver)
    page.open()
    page.login("standard_user", "wrong_password")
    assert page.is_error_displayed()
    assert "Epic sadface" in page.get_error_message()


@pytest.mark.negative
def test_login_with_empty_fields(driver):
    page = LoginPage(driver)
    page.open()
    page.login("", "")

    assert page.is_error_displayed()