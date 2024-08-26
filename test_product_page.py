from pages.product_page import ProductPage
import pytest
from pages.login_page import LoginPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

@pytest.mark.skip
@pytest.mark.parametrize('link', urls)
def  test_guest_add_product_to_basket_check_name_alert(browser,link):
    
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    current_product = page.get_product_name()
    product_name_in_alert = page.get_product_name_from_basket_alert()

    assert product_name_in_alert == current_product

@pytest.mark.skip
@pytest.mark.parametrize('link', urls)
def test_guest_add_product_to_basket_check_price_alert(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    current_price = page.get_product_price()
    product_price_in_alert = page.get_product_price_from_basket_alert()

    assert current_price == product_price_in_alert

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
#pytest -s --language=ru test_product_page.py