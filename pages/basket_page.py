from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_basket_empty(self):
        basket_empty_massage = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MASSAGE)
        basket_massage = basket_empty_massage.text
        assert basket_massage != None
    
    def check_basket_not_empty(self):
        basket_formset = self.browser.find_element(*BasketPageLocators.BASKET_FORMSET)
    
        assert basket_formset != None
    
