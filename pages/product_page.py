from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException 
import math
class ProductPage(BasePage):
    
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_massage_bassket(self):
        discount_name = self.browser.find_element(*ProductPageLocators.BASSKET_ALLERT_ADD_PRODUCT_DISCOUNT_ACTIVATE)
        return discount_name.text
    
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text
    
    def get_product_name_from_basket_alert(self):
        product_name_from_basket_alert = self.browser.find_element(*ProductPageLocators.BASSKET_ALLERT_PRODUCT_NAME)
        current_product = self.get_product_name()
        product_name_in_alert = product_name_from_basket_alert.text

        assert product_name_in_alert == current_product
    
    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text
    
    def get_product_price_from_basket_alert(self):
        product_price_basket_alert = self.browser.find_element(*ProductPageLocators.BASKET_ALERT_PRICE)
        current_price = self.get_product_price()
        product_price_in_alert = product_price_basket_alert.text
        
        assert current_price == product_price_in_alert
        
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message not disappeared"