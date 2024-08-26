from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini>span>a")
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    BASSKET_ALLERT_ADD_PRODUCT_DISCOUNT_ACTIVATE = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div > strong")
    BASSKET_ALLERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_ALERT_PRICE =(By.CSS_SELECTOR, ".alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div")

class BasketPageLocators():
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_EMPTY_MASSAGE = (By.CSS_SELECTOR, "#content_inner>p")