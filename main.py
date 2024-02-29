from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get("https://www.terabyteshop.com.br/hardware/processadores/intel")
time.sleep(10)

navegador.find_element(By.ID, "submitFormContinuar").click()




print(navegador)


elementos = navegador.find_elements(By.CLASS_NAME, 'prod-name')


print(elementos)
lista = []
for i in elementos:
    o = i.text
    lista.append(o)

        
    print(o)
print(lista)