from pages.product_page import ProductPage
import pytest
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from selenium.common.exceptions import NoSuchElementException
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        page.register_new_user(email, "Stepik123Step4-3")
        page.should_be_authorized_user()

    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_bassket_page()
        basket_page = BasketPage(browser, browser.current_url)
        try:
            basket_page.check_basket_not_empty()
        except NoSuchElementException:
            pass
        else:
            assert basket_page.check_basket_not_empty() == None
        basket_massage = basket_page.check_basket_empty()
        print(basket_massage)
        assert basket_massage != None
    
    def  test_user_add_product_to_basket_check_name_alert(self, browser):
        link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        #page.solve_quiz_and_get_code()

        current_product = page.get_product_name()
        product_name_in_alert = page.get_product_name_from_basket_alert()

        assert product_name_in_alert == current_product
#pytest -s --language=ru test_product_page.py::TestUserAddToBasketFromProductPage

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

@pytest.mark.xfail(reason="Geust not see items in basket ")
def test_guest_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_bassket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_items = basket_page.check_basket_not_empty()
    print (basket_items)
    assert basket_items != None

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_bassket_page()
    basket_page = BasketPage(browser, browser.current_url)
    try:
        basket_page.check_basket_not_empty()
    except NoSuchElementException:
        pass
    else:
        assert basket_page.check_basket_not_empty() == None
    basket_massage = basket_page.check_basket_empty()
    print(basket_massage)
    assert basket_massage != None

#pytest -s --language=ru test_product_page.py