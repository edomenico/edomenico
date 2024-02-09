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





def main():
    def redemet_baixa(escolha, ar, datahini, datahfim,estacao1):
        from datetime import datetime, timedelta
        import datetime
        import time
        if escolha == 1:
            from urllib.request import Request, urlopen
            #import lxml
            import pandas as pd
            import pandas as pd
            import time
            from datetime import datetime, timedelta
            from selenium import webdriver
            from bs4 import BeautifulSoup
            from selenium.webdriver.support.select import Select
            from selenium.webdriver.chrome.options import Options

            # datai = "01/06/2020 00:00"
            # dataf = "02/06/2020 23:00"
            datahi = datetime.strftime(datahini, '%d/%m/%Y %H:%M')
            datahf = datetime.strftime(datahfim, '%d/%m/%Y %H:%M')
            tempo = datahfim - datahini

            if datahi == datahf:
                intervalo = 0
            else:
                intervalo = int((str(tempo)[0:2]))
            mes = datahini.month
            # nome = "SBSC,SBAR,SBBH,SBBR,SBBV,SBCB,SBCG,SBCP,SBCT,SBCY,SBEN,SBES,SBFL,SBFN,SBFS,SBFZ,SBGL,SBGO,SBGR,SBIL,SBJF,SBJP,SBLB,SBME,SBMM,SBMO,SBMQ,SBNF,SBNT,SBPA,SBPJ,SBPV,SBRB,SBRF,SBRJ,SBSL,SBSP,SBST,SBSV,SBTE,SBMN,SBBE,SBVT,SBSG"
            nome = estacao1
            for i in range(intervalo + 1):
                # abre o Firefox
                #os.chdir("/mount/src/edomenico")
                #extension = 'exe'
                #all_filenames = [ii for ii in glob.glob('*.{}'.format(extension))]
                #browser = webdriver.Firefox(executable_path='all_filenames')
                # browser=webbrowser.open('https://redemet.decea.gov.br/?i=produtos&p=consulta-de-mensagens-opmet', new=2)
                # browser = webdriver.Chrome(executable_path='chrome.EXE')
                # chama a página da redemet para consulta

                



                from selenium.webdriver.firefox.service import Service

                gecko_path = "C:/geckodriver/geckodriver.exe"
                service = Service(gecko_path)
                driver = webdriver.Firefox(service=service)
                browser.get('https://redemet.decea.mil.br/old/modal/consulta-de-mensagens/')

                # browser.get('https://redemet.decea.gov.br/?i=produtos&p=consulta-de-mensagens-opmet')
                #browser.get('https://redemet.decea.mil.br/old/modal/consulta-de-mensagens/')
                #browser.get('https://redemet.decea.mil.br/old/modal/consulta-de-mensagens/')
                # browser.get('https://www.redemet.aer.mil.br/old/?i=produtos&p=consulta-de-mensagens-opmet')
                # if (datahi.day + i)==31:
                datacori = datahini + timedelta(days=i)
                    # datacori=datahf
                datacoris = datetime.strftime(datacori, '%d/%m/%Y %H:%M')


                datacori = datetime.strftime(datacori, '%d/%m/%Y %H:%M')
                datacorf=  datahfim + timedelta(hours=23)
                datacorfs = datetime.strftime(datacorf, '%d/%m/%Y %H:%M')
                datacorfs =datacorfs[0:10] + ' 23:00'

                # espera 5s
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
                # print(df[0])

                # print(table)
                if i == 0:
                    df = pd.read_html(str(table_html))
                    df = df[0]
                else:
                    df2 = pd.read_html(str(table_html))
                    df2 = df2[0]

                    df = df.append(df2, ignore_index=True)
                    print(df)

                # print(df.loc[(df["Localidade"] == 'SBSC')])
                df.to_csv("metar.csv", header=True)
                browser.quit()
            print(df)
            # df = df.drop(columns=['Unnamed: 0'])
            df.to_csv("metar.csv", header=True)
            # df.to_csv('example.csv')
        else:
            # importe a biblioteca usada para consultar uma URL
            import urllib.request
            import pandas as pd
            from datetime import datetime, timedelta
            # importe as funções BeautifulSoup para analisar os dados retornados do site
            from bs4 import BeautifulSoup

            # especifique o URL
            if ar == 1:
                wiki = "https://www.aviationweather.gov/metar/data?ids=SBJR%2CSBAC%2CSBAR%2CSBCB%2CSBCP%2CSBES%2CSBFN%2CSBFZ%2CSBGL%2CSBJE%2CSBJP%2CSBJU%2CSBKG%2CSBME%2CSBMO%2CSBMS%2CSBNT%2CSBPB%2CSBPJ%2CSBPL%2CSBPS%2CSBRF%2CSBRJ%2CSBSL%2CSBSG%2CSBTE%2CSBVT&format=raw&hours=72&taf=off&layout=on"
                # wiki="https://www.aviationweather.gov/metar/data?ids=sbfn&format=raw&hours=24&taf=off&layout=on"
            else:
                # wiki = "https://www.aviationweather.gov/metar/data?ids=SBRD%2CSBVH%2CSBJI%2CSBRB%2CSSKW%2CSBCY%2CSBPV%2CSBCZ%2CSBTT%2CSBIZ%2CSBCI%2CSBMA%2CSBCJ%2CSBHT%2CSBTB%2CSBOI%2CSWPI%2CSBBE%2CSBMQ%2CSBSN%2CSBSO%2CSBSI%2CSBAT%2CSBIH%2CSBMY%2CSBTF%2CSBUA%2CSBEG%2CSBBV&format=raw&date=&hours=24"
                wiki = "https://www.aviationweather.gov/metar/data?ids=SBRD,SBVH,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SWPI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SBTF,SBUA,SBEG,SBBV&format=raw&hours=72&taf=off&layout=on"
            # Consulte o site e retorne o html para a variável 'page'
            page = urllib.request.urlopen(wiki)

            # Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
            soup = BeautifulSoup(page, 'html5lib')
            # Insira a tag <li> e adicione sua classe
            list_item = soup.find_all('code')
            metar = []
            data = []

            metari = []
            dataaux = datetime.utcnow()
            dataaux = datetime.utcnow() - timedelta(hours=120)
            mesnow = datetime.utcnow().month
            mesant = (datetime.utcnow() - timedelta(hours=120)).month
            diaini = list_item[0].contents[0].split()[1][0:2]

            for i in range(len(list_item) - 1, -1, -1):
                if diaini >= list_item[i].contents[0].split()[1][0:2]:
                    # diaini = list_item[i].contents[0].split()[1][0:2]

                    dia = list_item[i].contents[0].split()[1][0:2]
                    mes = mesnow
                    ano = datetime.utcnow().year

                    dataini = str(dia) + '/' + str(mes) + '/' + str(ano)
                    datainicio = datetime.utcnow()
                    # datainicio = dataini.strftime('%d/%m/%Y')
                    data.append((dataini))
                    if int(list_item[i].string[9:11]) == 0:
                        metar.append([dataini, 'METAR ' + list_item[i].string + '='])
                    else:

                        metar.append([dataini, 'SPECI ' + list_item[i].string + '='])
            data_df = pd.DataFrame(metar, columns=['Data', 'Mensagem'])

            file = data_df.to_csv("metar.csv")

    start_date = datetime.today()
    end_date = datetime.today()

    area = ['Área 1', 'Área 2']
    area_1 = ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
              'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN', 'SBPL',
              'SBPJ']
    area_2 = ['SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA', 'SBCJ', 'SBHT',
              'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBMY', 'SBTF', 'SBUA', 'SBEG',
              'SBBV',
              'SSKW', 'SWEI', 'SWPI']
    st.set_page_config(
            page_title="Dados Estatísticos",
            page_icon="✅",
            layout="wide",
        )
    barra_lateral = st.sidebar.empty()
    area_seleciona = st.sidebar.selectbox("Seleciona a área:", area)
    if area_seleciona == 'Área 1':
        areasel = area_1
    else:
        areasel = area_2
    estacao = 'SBJR,SBAC,SBAR,SBCB,SBCP,SBES,SBFS,SBFN,SBFZ,SBGL,SBJE,SBJP,SBJU,SBKG,SBME,SBMO,SBMS,SBNT,SBPB,SBPJ,SBPL,SBPS,SBRF,SBRJ,SBSL,SBSG,SBTE,SBVT,'
    to_data = st.sidebar.date_input('Inicio:', start_date)
    from_data = st.sidebar.date_input('Fim:', end_date)
    if st.button('Carregar dados'):

        redemet_baixa(1, areasel, to_data, from_data,estacao)
       # st.button('Carregar dados')==False





if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
