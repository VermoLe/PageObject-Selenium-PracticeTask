from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_basket_empty(self):
        basket_empty_massage = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MASSAGE)
        return basket_empty_massage.text
    def check_basket_not_empty(self):
        basket_formset = self.browser.find_element(*BasketPageLocators.BASKET_FORMSET)
        return basket_formset
    
