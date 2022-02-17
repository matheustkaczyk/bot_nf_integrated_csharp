import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from dotenv import load_dotenv

load_dotenv('.env')

CPF = os.environ.get('CPF')
SENHA = os.environ.get('SENHA')
CEP = os.environ.get('CEP')
NCM = os.environ.get('NCM')
