import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

from path_index import login_index

load_dotenv('.env')

CPF = os.environ.get('CPF')
SENHA = os.environ.get('SENHA')
CEP = os.environ.get('CEP')
NCM = os.environ.get('NCM')
URL = os.environ.get('URL')

# Seta o driver do navegador como Firefox
# o driver entra com a URL especificada
driver = webdriver.Firefox()
driver.get(URL)

# Página de login
driver.find_element(By.XPATH, login_index['login_input'])
driver.find_element(By.XPATH, login_index['login_password'])
driver.find_element(By.XPATH, login_index['login_btn'])