from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://artflorboutique.com.br/")

sleep(3)
titulo_site = driver.title
if (titulo_site == 'Home - Artflor'):
    print('Sucesso')
else:
    print('Falha')
    print(titulo_site)

driver.quit()


