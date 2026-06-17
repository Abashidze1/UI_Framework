import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.fixture(autouse=False)
def products_page(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    return ProductsPage(driver)


@pytest.mark.smoke
def test_products_page_title(products_page):
    assert products_page.get_page_title() == "Products"


@pytest.mark.smoke
def test_products_count(products_page):
    assert products_page.get_products_count() == 6


@pytest.mark.positive
def test_add_product_to_cart(products_page):
    products_page.add_first_product_to_cart()
    assert products_page.is_cart_badge_displayed()
    assert products_page.get_cart_badge_count() == "1"


@pytest.mark.positive
def test_cart_badge_increments(products_page):
    products_page.add_first_product_to_cart()
    assert products_page.get_cart_badge_count() == "1"


@pytest.mark.positive
def test_sort_products_by_name_az(products_page):
    products_page.sort_products("az")
    names = products_page.get_product_names()
    assert names == sorted(names)


@pytest.mark.positive
def test_sort_products_by_name_za(products_page):
    products_page.sort_products("za")
    names = products_page.get_product_names()
    assert names == sorted(names, reverse=True)


@pytest.mark.positive
def test_go_to_cart(products_page):
    products_page.go_to_cart()
    assert "cart" in products_page.get_current_url()