from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()   #Перемудрили с абстракцией .is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
#pytest -v --tb=line --language=en test_main_page.py