from pages.product_page import ProductPage
import pytest

link =  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

@pytest.mark.xfail(reason="element is present")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="message not disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_message_disappeared()

#pytest -s --language=ru test_product_page_success_message.py
