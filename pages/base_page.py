from selenium import webdriver as RemoteWebDriver
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):            #Если буду использовать, убрать, потому что в стандартных исключениях видно из-за чего ошибка, да и  зачем это писать, челы серьёзно буквы в консоли читать не умеют или что 
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True