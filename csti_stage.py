from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Firefox
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
# servico = Service(GeckoDriverManager().install())
# navegador = webdriver.Firefox(service=servico)

# Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = str(os.getenv('SECRET_KEY'))
USER = str(os.getenv('USER'))

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)


def abrir_pagina(url):
    navegador.get(url)

def preencher_campo(xpath, conteudo):
    navegador.find_element(By.XPATH, xpath).send_keys(conteudo)

def clicar_campo(xpath):
    navegador.find_element(By.XPATH, xpath).click()


abrir_pagina('https://csti-stage.sorocaba.sp.gov.br/')

# Login
preencher_campo('//*[@id="User"]', USER)
preencher_campo('//*[@id="Password"]', SECRET_KEY)
clicar_campo('//*[@id="LoginButton"]')

# CMDB
clicar_campo('//*[@id="nav-CMDB"]/a')
clicar_campo('//*[@id="nav-CMDB-Overview"]/a')

# Sistemas
clicar_campo('//*[@id="OverviewControl"]/div/div[1]/ul[1]/li[8]/a')

# Lista de Sistemas:
elementos = navegador.find_elements(By.CLASS_NAME, 'MasterAction')
for elem in elementos:
    elem.click()

    # Editar
    clicar_campo('//*[@id="Menu300-Edit"]')

    # Troca para a janela ativa
    for handle in navegador.window_handles:
        navegador.switch_to.window(handle)

    # Salvar
    clicar_campo('//*[@id="SubmitButton"]')

    # Troca para a janela ativa
    for handle in navegador.window_handles:
        navegador.switch_to.window(handle)

    # Volta página
    navegador.back()
