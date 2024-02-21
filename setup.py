import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from datetime import datetime, timedelta
import datetime
import time

# Set up the Chrome driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def trata_redemet(areasele):
        
        import matplotlib.pyplot as plt
        import matplotlib.dates as md
        import dateutil

        import pandas as pd
        import os, sys
        import numpy as np
        from random import randint
        import re
        from datetime import datetime

        import string

        def criadataframe():
            global df,arqi
            COLUNAS = [
                'estacao',
                'datahora',
                'wspd',
                'wdir',
                'gust',
                'dryt',
                'dewp',
                'pres',
                'vis',
                'tp',
                'altn1',
                'qn1',
                'altn2',
                'qn2',
                'altn3',
                'qn3',
                'altn4',
                'qn4',
                'altncb',
                'qncb',
                'metar',
                'speci'
            ]

            df = pd.DataFrame(columns=COLUNAS)

        criadataframe()
        estado=areasele
        areatrab=areasele

        arqi = pd.read_csv('metar.csv',
                           sep=',',
                           # index_col=0,
                           parse_dates=True,
                           dayfirst=True,
                           decimal='.')
        wspd = []
        wdir = []
        estacao = []
        dryt = []
        dewp = []
        pres = []
        vis = []
        datahora = []
        altn1 = []
        altn2 = []
        altn3 = []
        altn4 = []
        altncb = []
        qn1 = []
        qn2 = []
        qn3 = []
        qn4 = []
        qncb = []
        tp = []
        gust = []
        k = -1
        metar=[]
        speci=[]


        for i in range(len(arqi)):

            if arqi.Mensagem[i] == 'METAR SBJR 171300Z 22002KT 9000 4000SW SCT010 SCT025 BKN040 24/21 Q1018=':
                c = 6

            if arqi.Mensagem[i].find('COR') > -1:
                novamens = 'METAR ' + arqi.Mensagem[i][arqi.Mensagem[i].find('COR') + 4:len(arqi.Mensagem[i])]


                mensagem1 = novamens.split()
                mens=novamens

            else:

                mensagem1 = arqi.Mensagem[i].split()
                mens=arqi.Mensagem[i]

            # print(len(mensagem1))

            if mensagem1[0] == 'METAR' or mensagem1[0]== 'SPECI':
                k = k + 1
                aviso = False
                entrou = False
                camada1 = False
                camada2 = False
                camada3 = False
                camada4 = False
                tempopres = False
                nuvemcb = False
                tempentrou = False

                for j in range(1, len(mensagem1), 1):

                    # if estacao[j] == 'SBFZ':
                    #     GGGGGGGGG = 1

                    if mensagem1[j].find('AUTO') > -1:
                        aviso = True
                    if j==2:
                        #data_hora=mensagem1[j][2:4]+':'+mensagem1[j][4:6]
                        data_hora = mensagem1[j][2:4] + ':00' #+ mensagem1[j][4:6]
                        if estacao[k] == 'SBFN' and data_hora == "20:00":
                            GGGGGGGGG = 1

                    # campo 3 vento
                    # arqi.Mensagem[i][arqi.Mensagem[i].find('KT')
                    if mensagem1[j].find('SB') > -1 or mensagem1[j].find('SSKW') > -1 or mensagem1[j].find('SWPI') > -1 or mensagem1[j].find('SWEI') > -1:
                        estacao.append(mensagem1[j])
                    # if estacao[k] == 'SBFZ':
                    #      GGGGGGGGG = 1

                    #if k==190:
                        #print('k= ',k,estacao[k])
                        #print('data',datahora[k-1])

                    if mensagem1[j].find('KT') > -1:
                        if len(wdir) == len(dryt):
                            if (mensagem1[j][0:3]) == 'VRB' or (mensagem1[j][0:3]) == '///' :

                                wdir.append('NaN')
                            else:
                                if mensagem1[j][0:3]=="OOO":
                                    wdir.append(0)
                                else:
                                    try:
                                        wdir.append(float(mensagem1[j][0:3]))
                                    except ValueError:
                                        wdir.append('NaN')

                            if (mensagem1[j][3:5]) == '//' or mensagem1[j].find('P') > -1:
                                wspd.append('NaN')
                            else:
                                if mensagem1[j][3:5]=='OO':
                                    wspd.append(0)
                                else:
                                    try:
                                        wspd.append(float(mensagem1[j][3:5]))
                                    except ValueError:
                                        wspd.append('NaN')

                            if mensagem1[j].find('G') > -1:
                                gust.append(mensagem1[j][6:8])
                            else:
                                gust.append('NaN')

                    if mensagem1[j].find('CAVOK') > -1 and aviso==False and entrou == False:

                        vis.append('9999')
                        entrou = True
                        altn1.append('NaN')
                        altn2.append('NaN')
                        altn3.append('NaN')
                        altn4.append('NaN')
                        qn1.append('NaN')
                        qn2.append('NaN')
                        qn3.append('NaN')
                        qn4.append('NaN')
                        camada1 = True
                        camada2 = True
                        camada3 = True
                        camada4 = True
                        print('cavok', mensagem1[j])

                    # sbxx data vento visi
                    if j == 4 and mensagem1[j].find('CAVOK') == -1 and aviso == False and mensagem1[j].find(
                            'V') == -1 and mensagem1[j].find('F')==-1 and mensagem1[j].find('S')==-1 and mensagem1[j].find('B')==-1 and mensagem1[j].find('O')==-1 and entrou == False:
                        vis.append(mensagem1[j])
                        entrou = True
                        print('j4 1', mensagem1[j])

                    # vento variavel nao cavok
                    if j == 5 and mensagem1[j - 1].find('V') > -1 and mensagem1[j].find('CAVOK') == -1 and mensagem1[
                        j - 1].find('CAVOK') == -1 and mensagem1[j].find('R') == -1 and entrou == False:
                        vis.append(mensagem1[j])
                        entrou = True
                        print('j5 1', mensagem1[j])

                    # automatica
                    if j == 5 and aviso == True and entrou == False and (mensagem1[j].find('V') == -1 or mensagem1[j].find('CAVOK') > -1):
                        if mensagem1[j].find('CAVOK') > -1:
                            vis.append('9999')
                            altn1.append('NaN')
                            altn2.append('NaN')
                            altn3.append('NaN')
                            altn4.append('NaN')
                            qn1.append('NaN')
                            qn2.append('NaN')
                            qn3.append('NaN')
                            qn4.append('NaN')
                            camada1 = True
                            camada2 = True
                            camada3 = True
                            camada4 = True
                        else:
                            vis.append(mensagem1[j])
                            print('j5 2',mensagem1[j])
                        entrou = True

                    if (mensagem1[j]==('////') and entrou == False) :
                        vis.append('NaN')
                        entrou=True



                    if j == 6 and aviso == True and entrou == False and mensagem1[j].find('/')==-1:
                        if mensagem1[j].find('CAVOK') > -1:
                            vis.append('9999')
                            altn1.append('NaN')
                            altn2.append('NaN')
                            altn3.append('NaN')
                            altn4.append('NaN')
                            qn1.append('NaN')
                            qn2.append('NaN')
                            qn3.append('NaN')
                            qn4.append('NaN')
                            camada1 = True
                            camada2 = True
                            camada3 = True
                            camada4 = True

                        else:
                            vis.append(mensagem1[j])
                        entrou = True



                    if mensagem1[j].find('Q') > -1 and mensagem1[j].find('S') !=0: #and bool(re.search(r'\d', mensagem1[j])):
                        if (mensagem1[j][1:5])=='////':
                            pres.append('NaN')
                        else:

                            try:
                           # print(mensagem1[j])

                                pres.append(float(mensagem1[j][1:5]))


                            except ValueError:
                                pres.append('NaN')
                                if len(pres)!=len(dryt):
                                    dryt.append('NaN')
                                if len(pres)!=len(dewp):
                                    dewp.append('NaN')


                        break

                    #if tempentrou== False:
                  #  if mensagem1[j].find('/') > -1 and bool(re.search(r'\d', mensagem1[j])) and mensagem1[j + 1].find(
                  #              'Q') > -1:
                   # print(mensagem1[j])
                    if mensagem1[j].find('/') > -1 and mensagem1[j + 1].find('Q') > -1:


                              # print(mensagem1[j][0:2])
                               # print(mensagem1[j][3:5])
                              #  print(mensagem1[j + 1])
                        if (mensagem1[j][0:2])=='//':

                            dryt.append('NaN')
                        else:
                            dryt.append(float(mensagem1[j][0:2]))
                        if (mensagem1[j][3:5]) == '//':
                            dewp.append('NaN')
                        else:
                            if mensagem1[j][3:5].find('M') > -1:
                                dewp.append(float(mensagem1[j][4:6])*-1)
                            else:

                                dewp.append(float(mensagem1[j][3:5]))
                                #tempentrou = True

                    if mensagem1[j].find('FEW') > -1 or mensagem1[j].find('SCT') > -1 or mensagem1[j].find('BKN') > -1 or \
                            mensagem1[j].find('OVC') > -1:
                        if mensagem1[j].find('CB') < 0 and mensagem1[j].find('TCU') < 0:
                            if camada1 == False:
                                if (mensagem1[j][3:6]).isnumeric():
                                    try:
                                        altn1.append(float(mensagem1[j][3:6]))
                                    except ValueError:
                                        altn1.append('NaN')
                                else:
                                    altn1.append((mensagem1[j][3:6]))
                                qn1.append((mensagem1[j][0:3]))
                                camada1 = True

                            elif camada2 == False:
                                if (mensagem1[j][3:6]).isnumeric():
                                    try:
                                        altn2.append(float(mensagem1[j][3:6]))
                                    except ValueError:
                                        altn2.append('NaN')

                                else:
                                    altn2.append((mensagem1[j][3:6]))
                                qn2.append((mensagem1[j][0:3]))
                                camada2 = True

                            elif camada3 == False:
                                if (mensagem1[j][3:5]).isnumeric():
                                    try:
                                        altn3.append(float(mensagem1[j][3:5]))
                                    except ValueError:
                                        altn3.append('NaN')
                                else:
                                    altn3.append((mensagem1[j][3:5]))
                                qn3.append((mensagem1[j][0:3]))
                                camada3 = True
                            else:

                                if (mensagem1[j][3:5]).isnumeric():
                                    altn4.append(float(mensagem1[j][3:5]))
                                else:
                                    altn4.append((mensagem1[j][3:5]))
                                qn4.append((mensagem1[j][0:3]))
                                camada4 = True
                    if mensagem1[j].find('CB') > -1 and len(mensagem1[j]) > 4 and nuvemcb==False:
                        altncb.append(((mensagem1[j][3:6])))
                        qncb.append((mensagem1[j][0:3]))
                        nuvemcb = True
                    if mensagem1[j].find('TCU') > -1 and len(mensagem1[j]) > 4 and nuvemcb==False:
                        altncb.append(((mensagem1[j][3:7])))
                        qncb.append((mensagem1[j][0:3]))
                        nuvemcb = True


                    if aviso == True and mensagem1[j].find('NCD') > -1:
                        altn1.append('NaN')
                        altn2.append('NaN')
                        altn3.append('NaN')
                        altn4.append('NaN')
                        qn1.append('NaN')
                        qn2.append('NaN')
                        qn3.append('NaN')
                        qn4.append('NaN')
                        camada1 = True
                        camada2 = True
                        camada3 = True
                        camada4 = True

                    if mensagem1[j].find('NSC') > -1:
                        altn1.append('NaN')
                        altn2.append('NaN')
                        altn3.append('NaN')
                        altn4.append('NaN')
                        qn1.append('NaN')
                        qn2.append('NaN')
                        qn3.append('NaN')
                        qn4.append('NaN')
                        camada1 = True
                        camada2 = True
                        camada3 = True
                        camada4 = True

                    if mensagem1[j].find('VV') > -1:
                        altn1.append((mensagem1[j][2:5]))
                        altn2.append('NaN')
                        altn3.append('NaN')
                        altn4.append('NaN')
                        qn1.append('OVC')
                        qn2.append('NaN')
                        qn3.append('NaN')
                        qn4.append('NaN')
                        camada1 = True
                        camada2 = True
                        camada3 = True
                        camada4 = True

                    if (mensagem1[j].find('RA') > -1 or mensagem1[j].find('DZ') > -1 or mensagem1[j].find('BR') > -1 or
                        mensagem1[j].find('HZ') > -1 or mensagem1[j].find('FG') > -1 or mensagem1[j].find('FU') > -1 or mensagem1[j].find('VC') > -1 or
                        mensagem1[j].find('TS') > -1) and mensagem1[j].find('SB') == -1 and mensagem1[j].find(
                            'OVC') == -1 and tempopres == False:
                        tp.append((mensagem1[j][0:len(mensagem1[j])]))
                        tempopres = True

                datahora.append(arqi['Data'][i]+' '+data_hora)
                try:
                    xhor = datetime.strptime(datahora[k], '%d/%m/%Y %H:%M')
                except ValueError:
                    if k > 0:
                        datahora[k] = datahora[k-1]
                else:
                    datahora[k]=xhor
                if nuvemcb == False:
                    altncb.append('NaN')
                    qncb.append('NaN')
                if camada1 == False:
                    altn1.append('NaN')
                    qn1.append('NaN')

                if camada2 == False:
                    altn2.append('NaN')
                    qn2.append('NaN')
                if camada3 == False:
                    altn3.append('NaN')
                    qn3.append('NaN')

                if camada4 == False:
                    altn4.append('NaN')
                    qn4.append('NaN')

                if (entrou == False):
                    vis.append('-10000')
                    entrou = True

                if tempopres == False:
                    tp.append('NaN')
                if len(dryt) != len(qn1):
                    print(estacao[k],datahora[k])
                if mensagem1[0] =='SPECI':
                    speci.append(mens)
                    print('aqui',datahora[k])
                    print(mens)
                    metar.append('-')
                else:
                    metar.append(mens)
                    speci.append('-')
                if estacao[k]=='SWPI':
                    yyyyyyyyy=1
                if vis[k]=='////':
                    vis[k]='-9999'
                if len(wspd) != len(pres):
                    pres.append('NaN')
                    if len(pres)!=len(dryt):
                        dryt.append('NaN')
                        dewp.append('NaN')
                df.loc[k] = [estacao[k]] + [datahora[k]] + [wspd[k]] + [wdir[k]] + [gust[k]] + [dryt[k]] + [dewp[k]] + [pres[k]] + [vis[k]] + [tp[k]] + [
                    altn1[k]] + [qn1[k]] + [altn2[k]] + [qn2[k]] + [altn3[k]] + [qn3[k]] + [altn4[k]] + [qn4[k]] + [
                            altncb[k]] + [qncb[k]] + [metar[k]] + [speci[k]]
                #f.sort_values(by=['First Column', 'Second Column', ...], inplace=True)


                df.sort_values(by=['estacao','datahora'], inplace=True)

                df.to_csv('metar_trat_'+str(estado)+'.csv',encoding='utf-8', index=False,date_format='%d/%m/%Y %H:%M')


        #-----------------------juntar arquivos
        arqiago = pd.read_csv('metar_trat_'+str(estado)+'.csv',
                              sep=',',
                              decimal='.')
        #x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in arqiago.datahora]
        #arqiago['data_hora'] = x
        if areatrab==1:
            
            arqiant = pd.read_csv('/mount/src/edomenico/metar_trat_teste1.csv',
                                sep=',',
                                decimal='.')
        else:
            
            arqiant = pd.read_csv('/mount/src/edomenico/metar_trat_teste2.csv',
                                  sep=',',
                                  decimal='.')


        df1 = pd.concat([arqiant, arqiago])
        df1.sort_values(by=['datahora', 'estacao'], inplace=True)
        df1 = df1.drop_duplicates(['estacao', 'datahora','speci'])

        if areatrab==1:
            df1.to_csv('metar_trat_teste1.csv', encoding='utf-8', index=False, date_format='%d/%m/%Y %H:%M')
        else:
            df1.to_csv('metar_trat_teste2.csv', encoding='utf-8', index=False, date_format='%d/%m/%Y %H:%M')

        return df1


    
    def redemet_baixa(escolha, ar, datahini, datahfim,estacao1):
        # Create Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
    
        # Create the driver with the options
        browser = webdriver.Chrome(options=chrome_options)
    
        # Load the page with Selenium
        #browser.get(url)
    
        # Wait up to 10 seconds for the page to load
        # Wait for the page to finish loading all JavaScript
        wait = WebDriverWait(browser, 20)


        
        
        if escolha == 1:
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
                #browser = webdriver.Firefox(executable_path='geckodriver.exe')
                # browser=webbrowser.open('https://redemet.decea.gov.br/?i=produtos&p=consulta-de-mensagens-opmet', new=2)
                # browser = webdriver.Chrome(executable_path='chrome.EXE')
                # chama a página da redemet para consulta

                # browser.get('https://redemet.decea.gov.br/?i=produtos&p=consulta-de-mensagens-opmet')
                browser.get('https://redemet.decea.mil.br/old/modal/consulta-de-mensagens/')
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
                time.sleep(15)
                # tira a checkbox para mensagem recente
                #driver.find_element(By.ID, url) 
                el = browser.find_element(By.ID, "consulta_recente")
                el.click()
                #browser.find_element_by_id("consulta_recente").click()

                # preenche o nome das estações para consulta
                
                element = browser.find_element(By.ID, "msg_localidade")
                element.send_keys(nome)

                # preenche a data inicial e final

                element = browser.find_element(By.ID, "consulta_data_ini").clear()
                
                element = browser.find_element(By.ID,"consulta_data_ini").click()
                element = browser.find_element(By.ID,"consulta_data_ini").send_keys(datacoris)
                element = browser.find_element(By.ID,"consulta_data_fim").clear()
                element = browser.find_element(By.ID,"consulta_data_fim").click()
                element = browser.find_element(By.ID,"consulta_data_fim").send_keys(datacorfs)

                # envia a consulta
                botao = browser.find_element(By.ID,"consulta_localidade")
                time.sleep(20)
                botao.click()

                # espera 10s
                time.sleep(20)

                ## coloca todo o resultado numa página
                # select_fr = Select(browser.find_element_by_name("msg_resultado_length"))
                # select_fr.select_by_index(3)

                table = browser.find_element(By.ID,'msg_resultado')

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
            os.chdir("/mount/src/edomenico/area1")
            df.to_csv("metar.csv", header=True)
            # df.to_csv('example.csv')
            return df
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
        areaprev=1
        areasel = area_1
       estacao = 'SBJR,SBAC,SBAR,SBCB,SBCP,SBES,SBFS,SBFN,SBFZ,SBGL,SBJE,SBJP,SBJU,SBKG,SBME,SBMO,SBMS,SBNT,SBPB,SBPJ,SBPL,SBPS,SBRF,SBRJ,SBSL,SBSG,SBTE,SBVT,'
    else:
        areaprev = 2
        areasel = area_2
        estacao = 'SBRD,SBVH,SWEI,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SWPI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SBTF,SBUA,SBEG,SBBV,'
    #estacao = 'SBJR,SBAC,SBAR,SBCB,SBCP,SBES,SBFS,SBFN,SBFZ,SBGL,SBJE,SBJP,SBJU,SBKG,SBME,SBMO,SBMS,SBNT,SBPB,SBPJ,SBPL,SBPS,SBRF,SBRJ,SBSL,SBSG,SBTE,SBVT,'
    to_data = st.sidebar.date_input('Inicio:', start_date)
    from_data = st.sidebar.date_input('Fim:', end_date)
    if st.button('Carregar dados'):
    
        pdf= redemet_baixa(1, areasel, to_data, from_data,estacao)
        #edited_df = st.data_editor(pdf)
        pdff=trata_redemet(areaprev)
        edited_df = st.data_editor(pdff)
if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
