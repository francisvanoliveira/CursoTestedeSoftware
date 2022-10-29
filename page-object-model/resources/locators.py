from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# class GooglePageLocators():
#     search_field = (By.NAME, 'q')
#     search_button = (By.NAME, 'btnK')


class ArtflorPageLocators():
    def teste_site(self):
        self.search_field = self.driver.title

class InovaPageLocators():
    def teste_site(self):
        self.search_field = self.driver.title
        
