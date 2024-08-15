from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

def test_guest_should_be_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

    #pytest -v --tb=line --language=en test_login_page.py
