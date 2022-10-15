#1 Acessar o site e realizar login
#2 Adicionar o produto mais barato no carrinho
#3 Comprar mais dois produtos
#4 Finalizar a compra

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

service = Service(executable_path="/usr/local/bin/chromedriver") ##carregar webdriver
driver = webdriver.Chrome(service=service) ##abre o navegador

driver.get("https://www.saucedemo.com")

campo_login = driver.find_element(By.ID, 'user-name')
campo_password = driver.find_element(By.ID, 'password')
login = driver.find_element(By.ID, 'login-button')

campo_login.send_keys('standard_user')
campo_password.send_keys('secret_sauce')
login.click()

sleep(5)

#add primeiro produto
lista_opcoes = driver.find_element(By.CLASS_NAME, 'product_sort_container')
select = Select(driver.find_element(
    By.CLASS_NAME, 'product_sort_container'))
select.select_by_index(2)
mais_barato = driver.find_element(
    By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
mais_barato.click()

#add segundo produto
lista_opcoes = driver.find_element(By.CLASS_NAME, 'product_sort_container')
select = Select(driver.find_element(
    By.CLASS_NAME, 'product_sort_container'))
select.select_by_index(1)
mais_barato = driver.find_element(
    By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
mais_barato.click()

#add terceiro produto
lista_opcoes = driver.find_element(By.CLASS_NAME, 'product_sort_container')
select = Select(driver.find_element(
    By.CLASS_NAME, 'product_sort_container'))
select.select_by_index(3)
mais_barato = driver.find_element(
    By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/button')
mais_barato.click()

#ir para o carrinho
campo_carrinho = driver.find_element(By.ID, 'shopping_cart_container')
campo_carrinho.click()

#preencher campos
campo_checkout = driver.find_element(By.ID, 'checkout')
campo_checkout.click()


first_name = driver.find_element(By.ID, 'first-name')
last_name = driver.find_element(By.ID, 'last-name')
postal_code = driver.find_element(By.ID, 'postal-code')
btn_continue = driver.find_element(By.ID, 'continue')

first_name.send_keys('Juquinha')
last_name.send_keys('Silveira')
postal_code.send_keys('69000-999')
btn_continue.click()

#finalizar
btn_finish = driver.find_element(By.ID, 'finish')
btn_finish.click()