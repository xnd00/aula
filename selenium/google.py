## pip install selenium
## pip install openpyxl
# Para fazer as automações
from selenium import webdriver
# Permite simular uso do teclado
from selenium.webdriver.common.keys import Keys
# Permite encontrar elementos
from selenium.webdriver.common.by import By
# Permite trabalhar com dropdown
from selenium.webdriver.support.select import Select
# Permite atrasar operação com tempo
from time import sleep
import openpyxl

from dados import acesso

us = acesso()[0]
psw= acesso()[1]

driver = webdriver.Chrome()
driver.maximize_window()
#driver.set_window_size(1250,780)
driver.get('https://www.google.com/')



# Pesquisar
# clicar em pesquisar
campo_pesquisar = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
campo_pesquisar.click()
sleep(2)
campo_pesquisar.send_keys('Estágio em direito em belo horizonte')
sleep(2)
campo_pesquisar.send_keys(Keys.ENTER)
sleep(3)


campo_mais100 = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div[2]/a/span[2]')
campo_mais100.click()

d = driver.find_element(By.TAG_NAME, "ul")
empresa =  driver.find_element(By.XPATH, "//div[@class='vNEEBe']")
cidade =  driver.find_element(By.XPATH, "//div[@class='Qk80Jf']")

print(d.text)



"""print('resultado: ')
for i in campo_ul:
    lista_ = driver.find_element(By.CLASS_NAME, "vNEEBe" )
    t = campo_ul.text
    print(t)"""

