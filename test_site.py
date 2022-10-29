import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep

# service = Service(executable_path="/usr/local/bin/chromedriver")
# driver = webdriver.Chrome(service=service)

# driver.get("https://artflorboutique.com.br/")

# sleep(3)
# titulo_site = driver.title
# if (titulo_site == 'Home - Artflor'):
#     print('Sucesso')
#     print(titulo_site)
# else:
#     print('Falha')
#     print(titulo_site)

# driver.quit()

class TesteSiteArtflor(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://artflorboutique.com.br/")

    def teste_site(self):
        self.titulo_site = self.driver.title
        if (self.titulo_site == 'Home - Artflor'):
           print('Sucesso')
           print(self.titulo_site)
        else:
           print('Falha')
           print(self.titulo_site)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

class TesteSiteInova(unittest.TestCase):
    def setUp(self):
        service = Service(executable_path="/usr/local/bin/chromedriver")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://inovameta.com.br/")

    def teste_site(self):
        self.titulo_site = self.driver.title
        if (self.titulo_site == 'Inovameta | Pesquisa, Desenvolvimento e Inovação'):
           print('Sucesso')
           print(self.titulo_site)
        else:
           print('Falha')
           print(self.titulo_site)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()