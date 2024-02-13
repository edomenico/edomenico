import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import sys
#from streamlit.web import cli as stcli

import streamlit
from streamlit import runtime
from streamlit_toggle import toggle
from streamlit.web import cli as stcli
import streamlit as st
from datetime import datetime, timedelta
import os
import glob
import requests

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager



def main():

    from urllib.request import Request, urlopen
            #import lxml
    import pandas as pd
    import pandas as pd
    import time
    from datetime import datetime, timedelta
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from selenium.webdriver.support.select import Select
    username = 'edomenico'
    token = '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'

   # login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))


   # curl -u username:token "https://api.github.com/repos/user/repo/issues?state=closed"
    URL = 'https://redemet.decea.mil.br/old/modal/consulta-de-mensagens/&access_token=token'
    datahi = "13/02/2024 00:00"
    datahf = "13/02/2024 00:00"
    #datahi = datetime.strftime(datai, '%d/%m/%Y %H:%M')
    #datahf = datetime.strftime(dataf, '%d/%m/%Y %H:%M')
    tempo = 0
    
    TIMEOUT = 20
    
    st.title("Test Selenium")
    st.markdown("Redemet about 21 seconds")
    
    firefoxOptions = Options()
    firefoxOptions.add_argument("--headless")
    service = Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(
        options=firefoxOptions,
        service=service,
    )
    if datahi == datahf:
        intervalo = 0
    else:
        intervalo = int((str(tempo)[0:2]))
    mes = datahini.month

    
    
    try:
        for i in range(intervalo + 1):
                
            #browser = webdriver.Firefox(executable_path='geckodriver.exe')
               
            browser.get(URL)
            browser.get(URL)
              
            datacori = datahini + timedelta(days=i)
                   
            datacoris = datetime.strftime(datacori, '%d/%m/%Y %H:%M')
            datacori = datetime.strftime(datacori, '%d/%m/%Y %H:%M')
            datacorf=  datahfim + timedelta(hours=23)
            datacorfs = datetime.strftime(datacorf, '%d/%m/%Y %H:%M')
            datacorfs =datacorfs[0:10] + ' 23:00'
            time.sleep(5)
     # tira a checkbox para mensagem recente
            browser.find_element_by_id("consulta_recente").click()

                # preenche o nome das estações para consulta
            element = browser.find_element_by_id("msg_localidade")
            element.send_keys(nome)

                # preenche a data inicial e final

            element = browser.find_element_by_id("consulta_data_ini").clear()
            element = browser.find_element_by_id("consulta_data_ini").click()
            element = browser.find_element_by_id("consulta_data_ini").send_keys(datacoris)
            element = browser.find_element_by_id("consulta_data_fim").clear()
            element = browser.find_element_by_id("consulta_data_fim").click()
            element = browser.find_element_by_id("consulta_data_fim").send_keys(datacorfs)
            # envia a consulta
            botao = browser.find_element_by_id("consulta_localidade")
            time.sleep(20)
            botao.click()

                # espera 10s
            time.sleep(20)

                ## coloca todo o resultado numa página
                # select_fr = Select(browser.find_element_by_name("msg_resultado_length"))
                # select_fr.select_by_index(3)

            table = browser.find_element_by_id('msg_resultado')

                # df = pd.read_html(str(table))
                # print(table)
            table_html = table.get_attribute('outerHTML')




            if i == 0:
                df = pd.read_html(str(table_html))
                df = df[0]
            else:
                df2 = pd.read_html(str(table_html))
                df2 = df2[0]

                df = df.append(df2, ignore_index=True)
                    

                # print(df.loc[(df["Localidade"] == 'SBSC')])
            df.to_csv("metar.csv", header=True)
            browser.quit()
            
            # df = df.drop(columns=['Unnamed: 0'])
        df.to_csv("metar.csv", header=True)
    
    except TimeoutException:
        st.warning("Timed out waiting for page to load")
        browser.quit()
    
    time.sleep(10)
    elements = driver.find_elements_by_xpath(XPATH)
    st.write([el.text for el in elements])
    browser.quit()




if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
