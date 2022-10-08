from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep

service = Service(executable_path="/usr/local/bin/chromedriver") ##carregar webdriver
browser = webdriver.Chrome(service=service) ##abre o navegador

browser.get('https://www.google.com')
sleep(2)
elemento = browser.find_element('tag name', 'input').send_keys("Scorpions")

botao = browser.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()