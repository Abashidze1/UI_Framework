import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@pytest.fixture()
def cart_page(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    products = ProductsPage(driver)
    products.add_first_product_to_cart()
    products.go_to_cart()

    return CartPage(driver)


@pytest.mark.smoke
def test_cart_page_title(cart_page):
    assert cart_page.get_page_title() == "Your Cart"


@pytest.mark.smoke
def test_cart_contains_added_item(cart_page):
    assert cart_page.get_cart_items_count() == 1


@pytest.mark.positive
def test_cart_item_has_name(cart_page):
    names = cart_page.get_item_names()
    assert len(names) == 1
    assert names[0] != ""


@pytest.mark.positive
def test_cart_item_has_price(cart_page):
    prices = cart_page.get_item_prices()
    assert len(prices) == 1
    assert "$" in prices[0]


@pytest.mark.positive
def test_remove_item_from_cart(cart_page):
    cart_page.remove_first_item()
    assert cart_page.is_empty()


@pytest.mark.positive
def test_continue_shopping_redirects(cart_page):
    cart_page.click_continue_shopping()
    assert "inventory" in cart_page.get_current_url()


@pytest.mark.positive
def test_checkout_button_redirects(cart_page):
    cart_page.click_checkout()
    assert "checkout-step-one" in cart_page.get_current_url()