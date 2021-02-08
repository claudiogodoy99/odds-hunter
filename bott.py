import os
import time
import re
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt

class newbot:

    def __init__(self, nome_bot):
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=options,executable_path=r'C:\chromedriver.exe')

    def coletarCotacoes(self):
        try:

            site  = 'https://www.betfair.com/br'
            self.driver.get(site)
            self.driver.implicitly_wait(20)
            
            self.driver.close()
        except:
            self.driver.close()
            self.erro()

    def erro(self):
         self.climaTempo()

    def salvaDados(self, dados):
        datt = datetime.now().date().strftime("%Y-%m-%d")
        arquivo = open('C:/ - ' + datt + '.txt', 'a')
        arquivo.write(dados + '\n')
        arquivo.close()











        
        
