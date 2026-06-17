import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture()
def checkout_page(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_first_product_to_cart()
    products.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    return CheckoutPage(driver)


@pytest.mark.smoke
def test_checkout_step_one_url(checkout_page):
    assert "checkout-step-one" in checkout_page.get_current_url()


@pytest.mark.positive
def test_complete_checkout(checkout_page):
    checkout_page.complete_checkout("George", "Smith", "123456")

    assert "checkout-complete" in checkout_page.get_current_url()
    assert "Thank you" in checkout_page.get_complete_header()


@pytest.mark.positive
def test_checkout_shows_total_price(checkout_page):
    checkout_page.fill_customer_info("George", "Smith", "123456")
    checkout_page.click_continue()

    total = checkout_page.get_total_price()
    assert "Total" in total
    assert "$" in total


@pytest.mark.positive
def test_cancel_returns_to_cart(checkout_page):
    checkout_page.click_cancel()
    assert "cart" in checkout_page.get_current_url()


@pytest.mark.negative
def test_checkout_empty_fields_shows_error(checkout_page):
    checkout_page.click_continue()

    assert checkout_page.is_error_displayed()
    assert "First Name is required" in checkout_page.get_error_message()


@pytest.mark.negative
def test_checkout_missing_zip_shows_error(checkout_page):
    checkout_page.fill_customer_info("George", "Smith", "")
    checkout_page.click_continue()

    assert checkout_page.is_error_displayed()
    assert "Postal Code is required" in checkout_page.get_error_message()