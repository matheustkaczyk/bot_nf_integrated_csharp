import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
from dotenv import load_dotenv
import json

# Importando arquivos de dicionário que contém XPATHS
from path_index import login_index, main_index, emition_index, receiver_index

load_dotenv('.env')

# Variáveis de ambiente
CPF = os.environ.get('CPF')
SENHA = os.environ.get('SENHA')
CEP = os.environ.get('CEP')
NCM = os.environ.get('NCM')
URL = os.environ.get('URL')

RUA = os.environ.get('RUA')
BAIRRO = os.environ.get('BAIRRO')
NUMERO = os.environ.get('NUMERO')

# Seta o driver do navegador como Firefox
# o driver entra com a URL especificada
driver = webdriver.Firefox()
driver.get(URL)

with open('clients.json') as clients:
  clients_json = list(json.load(clients).items())

  target_cnpj = '75578914000214'

  for client in clients_json:
    if client[1]['CNPJ'] == target_cnpj:
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

    # Tela de emissão

      time.sleep(.5)

      # Scroll para o fim da página para encontrar todos os itens
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

      time.sleep(.5)

      street_info_me = driver.find_element(By.XPATH, emition_index['street_info'])
      street_number_me = driver.find_element(By.XPATH, emition_index['street_number'])
      neighborhood_name_me = driver.find_element(By.XPATH, emition_index['neighborhood_name'])
      emition_btn = driver.find_element(By.XPATH, emition_index['emition_btn'])

      #Garantindo que os inputs estão vazios
      street_info_me.send_keys(Keys.CONTROL + 'a')
      street_info_me.send_keys(Keys.DELETE)
      street_number_me.send_keys(Keys.CONTROL + 'a')
      street_number_me.send_keys(Keys.DELETE)
      neighborhood_name_me.send_keys(Keys.CONTROL + 'a')
      neighborhood_name_me.send_keys(Keys.DELETE)
      #######################################

      street_info_me.send_keys(RUA)
      street_number_me.send_keys(NUMERO)
      neighborhood_name_me.send_keys(BAIRRO)

      time.sleep(.5)

      emition_btn.click()

      time.sleep(.5)

      # Tela identificação do recebidor

      # Identificação parte 1
      receiver_radio = driver.find_element(By.XPATH, receiver_index['receiver_type_btn'])
      receiver_cnpj_input = driver.find_element(By.XPATH, receiver_index['receiver_input_cnpj'])
      receiver_ie_input = driver.find_element(By.XPATH, receiver_index['receiver_ie'])
      receiver_fantasy_name = driver.find_element(By.XPATH, receiver_index['receiver_fantasy_name'])

      receiver_radio.click()
      time.sleep(1.5)

      receiver_cnpj_input.click()
      receiver_cnpj_input.send_keys(Keys.HOME + client[1]['CNPJ'])
      receiver_ie_input.send_keys(Keys.HOME + client[1]['IE'])
      receiver_fantasy_name.send_keys(Keys.HOME + client[1]['NOME_FANTASIA'])

      # Identificação parte 2

      # Scroll para o fim da página para encontrar todos os itens
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

      time.sleep(1)

      receiver_cep = driver.find_element(By.XPATH, receiver_index['receiver_cep'])
      receiver_street_info = driver.find_element(By.XPATH, receiver_index['receiver_street_info'])
      receiver_street_number = driver.find_element(By.XPATH, receiver_index['receiver_street_number'])
      receiver_neighborhood = driver.find_element(By.XPATH, receiver_index['receiver_neighborhood'])
      body = driver.find_element_by_tag_name('body');

      # Garante que é feito o fetch do CEP
      receiver_cep.click()
      receiver_cep.send_keys(Keys.HOME + CEP)
      body.click()
      ####################################