import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv

import time
import json

# Importando arquivos de dicionário que contém XPATHS
from path_index import (
    login_index,
    main_index,
    emition_index,
    receiver_index,
    identification_index,
    delivery_index,
    product_index,
    payment_index,
    transport_index,
    resume_index,
    done_index,
)

load_dotenv(".env")

# Variáveis de ambiente
CPF = os.environ.get("CPF")
SENHA = os.environ.get("SENHA")
CEP = os.environ.get("CEP")
NCM = os.environ.get("NCM")
CFOP = os.environ.get("CFOP")
UNIDADE = os.environ.get("UNIDADE")
URL = os.environ.get("URL")

RUA = os.environ.get("RUA")
BAIRRO = os.environ.get("BAIRRO")
NUMERO = os.environ.get("NUMERO")

# Descrição dos produtos
DESCRICAO3KG = os.environ.get("DESCRICAO3KG")
CODIGO3KG = os.environ.get("CODIGO3KG")

DESCRICAO5KG = os.environ.get("DESCRICAO5KG")
CODIGO5KG = os.environ.get("CODIGO5KG")
########################

# Informações de pagamento
PAGAMENTO = os.environ.get("PAGAMENTO")
FORMAPAGAMENTO = os.environ.get("FORMAPAGAMENTO")
##########################

# Seta o driver do navegador como Firefox
# o driver entra com a URL especificada
driver = webdriver.Chrome()
driver.minimize_window()
driver.get(URL)

with open("clients.json") as clients:
    clients_json = list(json.load(clients).items())

    print("Inicializando o bot")
    print("===================")
    print('Informações cadastradas: \n')
    for client in clients_json:
        print(client[1]["NOME_FANTASIA"], client[1]['CNPJ'],client[1]['VALOR'])

    target_cnpj = input("Insira o CNPJ desejado (apenas os números): ")
    ask_5kg = input("Pacote de 5KG? (sim ou não): ")

    if target_cnpj != "":
        quantity3kg = input("Digite a quantidade desejada (3KG): ")

        if ask_5kg not in ["false", "no", "não", "n"]:
            quantity5kg = input("Digite a quantidade desejada (5KG): ")
            price5kg = input("Digite o preço unitário do pacote (5KG): ")

        for client in clients_json:
            if client[1]["CNPJ"] == target_cnpj:
                # Página de login elementos
                time.sleep(0.5)

                input_login = driver.find_element(By.XPATH, login_index["login_input"])
                input_password_login = driver.find_element(
                    By.XPATH, login_index["login_password"]
                )
                login_btn = driver.find_element(By.XPATH, login_index["login_btn"])

                input_login.send_keys(CPF)
                input_password_login.send_keys(SENHA)
                login_btn.click()

                # Tela principal

                time.sleep(0.5)

                main_selector_wrapper = driver.find_element(
                    By.XPATH, main_index["main_selector_wrapper"]
                )
                main_selector_wrapper.click()

                time.sleep(1)

                main_selector = driver.find_element(
                    By.XPATH, main_index["main_selector"]
                )
                main_selector.click()

                # Tela de emissão

                time.sleep(0.5)

                # Scroll para o fim da página para encontrar todos os itens
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                time.sleep(0.5)

                street_info_me = driver.find_element(
                    By.XPATH, emition_index["street_info"]
                )
                street_number_me = driver.find_element(
                    By.XPATH, emition_index["street_number"]
                )
                neighborhood_name_me = driver.find_element(
                    By.XPATH, emition_index["neighborhood_name"]
                )
                emition_btn = driver.find_element(
                    By.XPATH, emition_index["emition_btn"]
                )

                # Garantindo que os inputs estão vazios
                street_info_me.send_keys(Keys.CONTROL + "a")
                street_info_me.send_keys(Keys.DELETE)
                street_number_me.send_keys(Keys.CONTROL + "a")
                street_number_me.send_keys(Keys.DELETE)
                neighborhood_name_me.send_keys(Keys.CONTROL + "a")
                neighborhood_name_me.send_keys(Keys.DELETE)
                #######################################

                street_info_me.send_keys(RUA)
                street_number_me.send_keys(NUMERO)
                neighborhood_name_me.send_keys(BAIRRO)

                time.sleep(0.5)

                emition_btn.click()

                time.sleep(0.5)

                # Tela identificação do recebidor

                # Identificação parte 1
                receiver_radio = driver.find_element(
                    By.XPATH, receiver_index["receiver_type_btn"]
                )
                receiver_ie_input = driver.find_element(
                    By.XPATH, receiver_index["receiver_ie"]
                )
                receiver_fantasy_name = driver.find_element(
                    By.XPATH, receiver_index["receiver_fantasy_name"]
                )

                receiver_radio.click()

                time.sleep(2)

                # Página re-renderiza
                receiver_cnpj_input = driver.find_element(
                    By.XPATH, receiver_index["receiver_input_cnpj"]
                )

                receiver_cnpj_input.click()
                receiver_cnpj_input.send_keys(Keys.HOME + client[1]["CNPJ"])
                receiver_ie_input.send_keys(client[1]["IE"])
                receiver_fantasy_name.send_keys(client[1]["NOME_FANTASIA"])

                # Identificação parte 2
                time.sleep(1)

                # Scroll para o fim da página para encontrar todos os itens
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                time.sleep(0.5)

                receiver_cep = driver.find_element(
                    By.XPATH, receiver_index["receiver_cep"]
                )
                receiver_street_info = driver.find_element(
                    By.XPATH, receiver_index["receiver_street_info"]
                )
                receiver_street_number = driver.find_element(
                    By.XPATH, receiver_index["receiver_street_number"]
                )
                receiver_neighborhood = driver.find_element(
                    By.XPATH, receiver_index["receiver_neighborhood"]
                )
                receiver_btn = driver.find_element(
                    By.XPATH, receiver_index["receiver_btn"]
                )

                time.sleep(0.5)

                # # Garante que é feito o fetch do CEP
                receiver_cep.click()
                receiver_cep.send_keys(Keys.HOME + CEP)

                time.sleep(1)
                receiver_street_info.click()
                # ####################################

                time.sleep(4)
                receiver_street_info.send_keys(client[1]["LOGRADOURO"])
                receiver_street_number.send_keys(client[1]["NUMERO"])
                receiver_neighborhood.send_keys(client[1]["BAIRRO"])

                time.sleep(0.5)
                receiver_btn.click()
                time.sleep(0.5)

                # Tela de Identificação da nota

                # Todos os selects da página
                operation_nature = driver.find_element(
                    By.XPATH, identification_index["nature_operation"]
                )
                operation_type = Select(
                    driver.find_element(
                        By.XPATH, identification_index["operation_type_select"]
                    )
                )
                operation_finality = Select(
                    driver.find_element(
                        By.XPATH, identification_index["operation_finality"]
                    )
                )
                operation_presence = Select(
                    driver.find_element(
                        By.XPATH, identification_index["operation_presence"]
                    )
                )
                ############################

                time.sleep(0.5)

                # operation_nature não é um select, então deve-se fazer manualmente
                operation_nature.click()

                time.sleep(0.5)

                operation_nature_opt = driver.find_element(
                    By.XPATH, identification_index["nature_operation_opt"]
                )
                operation_nature_opt.click()
                #########################################################################

                time.sleep(0.5)

                operation_type.select_by_visible_text("1 - Saída")
                operation_finality.select_by_visible_text("1 - NF-e normal")
                operation_presence.select_by_visible_text("1 - Operação presencial")

                time.sleep(1)

                # Scrolla até o fim da página para encontrar o botão
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                time.sleep(1)

                operation_btn = driver.find_element(
                    By.XPATH, identification_index["operation_btn"]
                )
                operation_btn.click()

                # Tela entrega
                time.sleep(0.5)

                delivery_btn = driver.find_element(
                    By.XPATH, delivery_index["delivery_btn"]
                )
                delivery_btn.click()
                #################################

                # Tela de produto
                time.sleep(1)

                product_description = driver.find_element(
                    By.XPATH, product_index["product_description"]
                )
                product_code = driver.find_element(
                    By.XPATH, product_index["product_code"]
                )
                product_ncm = driver.find_element(
                    By.XPATH, product_index["product_ncm"]
                )
                product_cfop = Select(
                    driver.find_element(By.XPATH, product_index["product_cfop_select"])
                )
                product_unity = driver.find_element(
                    By.XPATH, product_index["product_unity"]
                )
                product_quantity = driver.find_element(
                    By.XPATH, product_index["product_quantity"]
                )
                product_value = driver.find_element(
                    By.XPATH, product_index["product_value"]
                )

                time.sleep(0.5)

                product_description.send_keys(DESCRICAO3KG)
                product_code.send_keys(CODIGO3KG)
                product_ncm.send_keys(NCM)
                product_cfop.select_by_visible_text(CFOP)
                product_unity.send_keys(UNIDADE)
                product_quantity.send_keys(Keys.HOME + quantity3kg)
                product_value.send_keys(Keys.HOME + client[1]["VALOR"])

                time.sleep(1)

                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                time.sleep(0.5)

                product_btn = driver.find_element(
                    By.XPATH, product_index["product_btn"]
                )
                product_btn.click()
                ##################################3

                time.sleep(1)

                # Faz a verificação se há a necessidade de emitir pacotes de 5kg
                if ask_5kg in ["yes", "y", "true", "t"]:
                    new_product_btn = driver.find_element(
                        By.XPATH, product_index["new_product_btn"]
                    )
                    new_product_btn.click()

                    time.sleep(1)

                    product_description = driver.find_element(
                        By.XPATH, product_index["product_description"]
                    )
                    product_code = driver.find_element(
                        By.XPATH, product_index["product_code"]
                    )
                    product_ncm = driver.find_element(
                        By.XPATH, product_index["product_ncm"]
                    )
                    product_cfop = Select(
                        driver.find_element(
                            By.XPATH, product_index["product_cfop_select"]
                        )
                    )
                    product_unity = driver.find_element(
                        By.XPATH, product_index["product_unity"]
                    )
                    product_quantity = driver.find_element(
                        By.XPATH, product_index["product_quantity"]
                    )
                    product_value = driver.find_element(
                        By.XPATH, product_index["product_value"]
                    )

                    time.sleep(1)

                    product_description.send_keys(DESCRICAO5KG)
                    product_code.send_keys(CODIGO5KG)
                    product_ncm.send_keys(NCM)
                    product_cfop.select_by_visible_text(CFOP)
                    product_unity.send_keys(UNIDADE)
                    product_quantity.send_keys(Keys.HOME + quantity5kg)
                    product_value.send_keys(Keys.HOME + price5kg)

                    time.sleep(1)

                    driver.execute_script(
                        "window.scrollTo(0,document.body.scrollHeight)"
                    )

                    time.sleep(0.5)

                    product_btn = driver.find_element(
                        By.XPATH, product_index["product_btn"]
                    )
                    product_btn.click()

                time.sleep(1)

                product_next = driver.find_element(
                    By.XPATH, product_index["product_btn_next"]
                )
                product_next.click()

                # Tela de pagamento

                time.sleep(1)

                # Captura o valor total do input disabled
                total_value = driver.find_element(
                    By.XPATH, payment_index["payment_total_input"]
                ).get_attribute("value")
                payment_add_btn = driver.find_element(
                    By.XPATH, payment_index["payment_add_btn"]
                )

                time.sleep(0.5)

                payment_add_btn.click()

                time.sleep(1)

                payment_method_select = Select(
                    driver.find_element(
                        By.XPATH, payment_index["payment_method_select"]
                    )
                )
                payment_type_select = Select(
                    driver.find_element(By.XPATH, payment_index["payment_type_select"])
                )
                payment_value = driver.find_element(
                    By.XPATH, payment_index["payment_value"]
                )
                payment_btn_save = driver.find_element(
                    By.XPATH, payment_index["payment_btn_save"]
                )

                time.sleep(0.5)

                # Seta os selects e o valor total capturado
                payment_method_select.select_by_visible_text(PAGAMENTO)
                payment_type_select.select_by_visible_text(FORMAPAGAMENTO)
                payment_value.send_keys(Keys.HOME + total_value)
                payment_btn_save.click()

                time.sleep(0.5)

                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                payment_next_btn = driver.find_element(
                    By.XPATH, payment_index["payment_btn"]
                )
                payment_next_btn.click()

                time.sleep(1)

                # Página de transporte

                transport_type_select = Select(
                    driver.find_element(
                        By.XPATH, transport_index["transport_type_select"]
                    )
                )
                transport_type_select.select_by_visible_text(
                    "3 - Transporte Próprio por conta do Remetente"
                )

                time.sleep(0.5)

                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                transport_btn = driver.find_element(
                    By.XPATH, transport_index["transport_btn"]
                )
                transport_btn.click()

                # Tela de resumo

                time.sleep(1)

                driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                time.sleep(1)

                resume_btn = driver.find_element(By.XPATH, resume_index["resume_btn"])

                time.sleep(0.5)

                resume_btn.click()

                time.sleep(1)

                confirmation_span = driver.find_element(
                    By.XPATH, done_index["confirmation_span"]
                )
                if confirmation_span.text == "AUTORIZADA":
                    print("NF emitida com sucesso!")
