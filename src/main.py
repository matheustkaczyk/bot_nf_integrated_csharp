import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

import time
import json
# import org.openqa.selenium.support.ui.Select

# Importando arquivos de dicionário que contém XPATHS
from path_index import login_index, main_index, emition_index, receiver_index, identification_index

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

  target_cnpj = '10602819000263'

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
      time.sleep(2)

      receiver_cnpj_input.click()
      receiver_cnpj_input.send_keys(Keys.HOME + client[1]['CNPJ'])
      receiver_ie_input.send_keys(client[1]['IE'])
      receiver_fantasy_name.send_keys(client[1]['NOME_FANTASIA'])

      # Identificação parte 2
      time.sleep(1)

      # Scroll para o fim da página para encontrar todos os itens
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

      time.sleep(.5)

      receiver_cep = driver.find_element(By.XPATH, receiver_index['receiver_cep'])
      receiver_street_info = driver.find_element(By.XPATH, receiver_index['receiver_street_info'])
      receiver_street_number = driver.find_element(By.XPATH, receiver_index['receiver_street_number'])
      receiver_neighborhood = driver.find_element(By.XPATH, receiver_index['receiver_neighborhood'])
      receiver_btn = driver.find_element(By.XPATH, receiver_index['receiver_btn'])
      time.sleep(.5)

      # # Garante que é feito o fetch do CEP
      receiver_cep.click()
      receiver_cep.send_keys(Keys.HOME + CEP)

      time.sleep(1)
      receiver_street_info.click()
      # ####################################

      time.sleep(.5)
      receiver_street_info.send_keys(client[1]['LOGRADOURO'])
      receiver_street_number.send_keys(client[1]['NUMERO'])
      receiver_neighborhood.send_keys(client[1]['BAIRRO'])
      
      time.sleep(.5)
      receiver_btn.click()
      time.sleep(.5)

      # Tela de Identificação da nota

      # Todos os selects da página
      operation_nature = driver.find_element(By.XPATH, identification_index['nature_operation'])
      operation_type = driver.find_element(By.XPATH, identification_index['operation_type_select'])
      operation_finality = driver.find_element(By.XPATH, identification_index['operation_finality'])
      operation_presence = driver.find_element(By.XPATH, identification_index['operation_presence'])
      ############################

      time.sleep(.5)

      # operation_nature.click()

      # time.sleep(1)

      # operation_nature_opt = driver = driver.find_element(By.XPATH, identification_index['nature_operation_opt'])
      # operation_nature_opt.click()

      # time.sleep(.5)

      # operation_type.click()

      # time.sleep(.5)

      # operation_type_opt = driver.find_element(By.XPATH, identification_index['operation_type_select_opt'])
      # operation_type_opt.click()

      # time.sleep(.5)

      # operation_finality.click()

      # time.sleep(.5)

      # operation_finality_opt = driver.find_element(By.XPATH, identification_index['operation_finality_opt'])
      # operation_finality_opt.click()

      # time.sleep(.5)

      # operation_presence.click()

      # time.sleep(.5)

      # operation_presence_opt = driver.find_element(By.XPATH, identification_index['operation_presence_opt'])
      # operation_presence_opt.click()

      # time.sleep(.5)

      # Scrolla até o fim da página para encontrar o botão
      driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

      operation_btn = driver.find_element(By.XPATH, identification_index['operation_btn'])
      operation_btn.click()