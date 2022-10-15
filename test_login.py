import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ProcedimentoTesteLogin(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path="/usr/local/bin/chromedriver") ##carregar webdriver
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.saucedemo.com/")

    def test_login_invalido(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_password = self.driver.find_element(By.ID, 'password')
        login = self.driver.find_element(By.ID, 'login-button')

        # ENTRADA
        campo_login.send_keys('user')
        campo_password.send_keys('secret_sauce')
        login.click()
        # SAIDA ESPERADA
        elemento_erro = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertTrue(elemento_erro.is_displayed())

    def test_login_vazio(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_password = self.driver.find_element(By.ID, 'password')
        login = self.driver.find_element(By.ID, 'login-button')

        # ENTRADO
        campo_login.send_keys('')
        campo_password.send_keys('secret_sauce')
        login.click()
        # SAIDA ESPERADA
        elemento_erro = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        self.assertTrue(elemento_erro.is_displayed())

    def test_senha_invalido(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_password = self.driver.find_element(By.ID, 'password')
        login = self.driver.find_element(By.ID, 'login-button')

        # ENTRADA
        campo_login.send_keys('standard_user')
        campo_password.send_keys('secret')
        login.click()
        # SAIDA ESPERADA
        elemento_erro = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertTrue(elemento_erro.is_displayed())

    def test_senha_vazia(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_password = self.driver.find_element(By.ID, 'password')
        login = self.driver.find_element(By.ID, 'login-button')

        # ENTRADA
        campo_login.send_keys('standard_user')
        campo_password.send_keys('')
        login.click()
        # SAIDA ESPERADA
        elemento_erro = self.driver.find_element(
            By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]')
        self.assertTrue(elemento_erro.is_displayed())

    def test_login_senha_valida(self):
        campo_login = self.driver.find_element(By.ID, 'user-name')
        campo_password = self.driver.find_element(By.ID, 'password')
        login = self.driver.find_element(By.ID, 'login-button')

        # ENTRADA
        campo_login.send_keys('standard_user')
        campo_password.send_keys('secret_sauce')
        login.click()
        # SAIDA ESPERADA
        elemento_erro = self.driver.find_element(
            By.XPATH, '//*[@id="page_wrapper"]')
        self.assertTrue(elemento_erro.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()