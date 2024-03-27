from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Pc:
    def __init__(self) :
        options = uc.ChromeOptions()
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--no-first-run')
        options.add_argument("--window-size=2560,1440")
        options.add_argument('--no-sandbox')
        self.navegador = uc.Chrome(options=options,version_main=123)
        self.navegador.get("https://www.terabyteshop.com.br/")
        time.sleep(10)
        self.navegador.find_element(By.ID, "submitFormContinuar").click()
    def funcao_principal(self):
        # envia_banco = []
        # envia_banco.append(self.processador())
        self.placa_mae()


    def processador(self):
        self.navegador.get('https://www.terabyteshop.com.br/hardware/processadores/intel')
        elementos = self.navegador.find_elements(By.CLASS_NAME, 'commerce_columns_item_image')

        print(elementos)
        processador = []
        for i in elementos:
            if i.text.find('\nAVISE-ME') >1:
                break
            try:
                o = i.text
                descricao = i.text.split('\n')[0]
                valor = o.split('R$ ')[1].split(' ')[0]
                arr = {'descricao': descricao, 'valor': valor}
                processador.append(arr)
            except:
                break
        return processador

    def pega_links(self):
        links = []
        self.navegador.get('https://www.terabyteshop.com.br/hardware/placas-mae/lga-1700-intel')
        elementos = self.navegador.find_elements(By.CLASS_NAME, 'commerce_columns_item_inner')
        for placa in elementos:
            try:
                placa.find_element(By.CLASS_NAME, 'tbt_esgotado')
                break
            except:
                link = placa.find_element(By.CLASS_NAME, 'commerce_columns_item_image').get_attribute('href')
                links.append(link)
        self.placa_mae(links)


    def placa_mae(self, links):



        descricao = []
        for link in links:
            self.navegador.get(link)
            # o = link.text
            # descricao = link.text.split('\n')[0]
            # valor = o.split('R$ ')[1].split(' ')[0]
            # self.navegador.find_element(By.CSS_SELECTOR,  ".pbox:nth-child(2) h2").click()
            self.navegador.execute_script("window.scrollTo(0,1560)")
            self.navegador.execute_script("window.scrollTo(0,2640)")
            self.navegador.execute_script("window.scrollTo(0,3100)")
            # WebDriverWait(self.navegador, 6).until(EC.visibility_of_element_located((By.CLASS_NAME, "collapsed accordion-toggle"))).click()
            try:
                WebDriverWait(self.navegador, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#body > div:nth-child(6) > div > div:nth-child(4) > div > div.panel-heading > p > a"))).click()
            except:
                WebDriverWait(self.navegador, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#body > div:nth-child(7) > div > div:nth-child(4) > div > div.panel-heading > p > a"))).click()

            # WebDriverWait(self.navegador, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,  "#body > div:nth-child(6) > div > div:nth-child(4) > div > div.panel-heading > p > a"))).click()
            # self.navegador.find_element(By.CSS_SELECTOR,  "#body > div:nth-child(6) > div > div:nth-child(4) > div > div.panel-heading > p > a").click()
            suporte = self.navegador.find_element(By.CLASS_NAME, 'tecnicas').text.split('\nCPU:\n')[1].split('*')[0]
            # descricao_item = self.navegador.find_element(By.CLASS_NAME, 'tecnicas').text.split('\nCPU:\n')[1].split('*')[0].strip().split(':')[1]
            arr = {'suporte_placa': suporte}
            descricao.append(arr)
        return descricao



            # arr = {'descricao': descricao, 'valor': valor}
            # placas.append(arr)


        

        