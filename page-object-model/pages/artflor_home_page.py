
from pages.base_page import BasePage
from resources.locators import ArtflorPageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://artflorboutique.com.br/')

    def search_info(self, info):
        self.get_title(ArtflorPageLocators.teste_site.search_field, info)
    
