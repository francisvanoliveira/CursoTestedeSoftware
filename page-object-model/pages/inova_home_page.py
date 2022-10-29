
from pages.base_page import BasePage
from resources.locators import InovaPageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://inovameta.com.br/')

    def search_info(self, info):
        self.get_title(InovaPageLocators.teste_site.search_field, info)
    
