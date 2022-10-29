import unittest

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

from pages.inova_home_page import HomePage


class TestArtflorHomePage(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.home_page = HomePage(self.driver)

    def test_search_info(self):
        #self.home_page.search_info()
        resultado_obtido = self.home_page.get_title()
        self.assertIn('Inovameta | Pesquisa, Desenvolvimento e Inovação', resultado_obtido)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
