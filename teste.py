##Código em puyhton para utilizar selenium e chromedriver 

from selenium.webdriver.chrome.service import Service
from selenium import webdriver

service = Service(executable_path="/usr/local/bin/chromedriver") ##carregar webdriver
driver = webdriver.Chrome(service=service) ##abre o navegador