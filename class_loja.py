from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


class Pc:
    def __init__(self) :

        self.navegador = webdriver.Chrome()
        self.navegador.get("https://www.terabyteshop.com.br/")
        time.sleep(10)
        self.navegador.find_element(By.ID, "submitFormContinuar").click()
    def funcao_principal(self):
        envia_banco = []
        envia_banco.append(self.processador())
        self.placa_mae()


    def processador(self):
        self.navegador.get('https://www.terabyteshop.com.br/hardware/processadores/intel')
        elementos = self.navegador.find_elements(By.CLASS_NAME, 'commerce_columns_item_inner')

        print(elementos)
        processador = []
        for i in elementos:
            if i.text.find('\nAVISE-ME') >1:
                break
            o = i.text
            descricao = i.text.split('\n')[0]
            valor = o.split('R$ ')[1].split(' ')[0]
            arr = {'descricao': descricao, 'valor': valor}
            processador.append(arr)
        return processador

    def placa_mae(self):
        self.navegador.get('https://www.terabyteshop.com.br/hardware/placas-mae/lga-1700-intel')
        

        