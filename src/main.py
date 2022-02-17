import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from dotenv import load_dotenv
import json

# Importando arquivos de dicionário que contém XPATHS
from path_index import login_index, main_index

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

with open('clients.json') as clients:
  jsonClients = list(json.load(clients).items())
  clients.close()

# Página de login elementos
  time.sleep(.5)

  input_login = driver.find_element(By.XPATH, login_index['login_input'])
  input_password_login = driver.find_element(By.XPATH, login_index['login_password'])
  login_btn = driver.find_element(By.XPATH, login_index['login_btn'])

  input_login.send_keys(CPF)
  input_password_login.send_keys(SENHA)
  login_btn.click()

# Tela principal

  time.sleep(.5)

  main_selector_wrapper = driver.find_element(By.XPATH, main_index['main_selector_wrapper'])
  main_selector_wrapper.click()

  time.sleep(1)

  main_selector = driver.find_element(By.XPATH, main_index['main_selector'])
  main_selector.click()
