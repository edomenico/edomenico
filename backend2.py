import requests
import pandas as pd
import streamlit as st
import baixarmodeloNovoprojeto
import baixaamodeloNovometeograma



import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime,timedelta
from datetime import date
from pytz import timezone
import re
from bs4 import BeautifulSoup

import pandas as pd
from datetime import datetime, timedelta
import datetime
import time
        
# Set up the Chrome driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
def import re
import urllib.parse
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime,timedelta
from datetime import date
from pytz import timezone
import re
from bs4 import BeautifulSoup

import pandas as pd
from datetime import datetime, timedelta
import datetime
import time
        
# Set up the Chrome driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType


def qnuvem(s):
    nuvcb='n'
    nuv=''
    tp=''
    vis=''
    if s=='1':
        nuv='CAVOK'
        vis='9999'
        tp=''
    elif s=='2':
        nuv='FEW'
        vis = '9999'
        tp=''
    elif s=='3' or s=='4':#PARC NUBLADO
        nuv='SCT'
        vis = '9999'
        tp=''

    elif s == '5' or s=='18' : #'CHUVA FRACA'
        nuv = 'SCT'
        tp=''
        vis = '7000'
    elif s == '6' or s == '7' : #'CHUVA MODERADA'
        nuv = 'BKN'
        tp='RA'
        vis = '3500'


    elif s=='17': #NÉVOA
        nuv = 'BKN'
        tp = 'BR'
        vis = '3500'
    elif s == '14' or s == '21': #|TROVOADA COM CHUVA
        nuv = 'BKN'
        nuvcb='s'
        tp = 'TS'
        vis = '7000'
    elif s == '22': # #NÉVOA
        nuv = 'SCT'
        tp = 'BR'
        vis = '4000'
    elif s == '20' or s == '19':# #CHUVA FRACA
        nuv = 'BKN'
        tp = 'BR'
        vis = '4000'
    elif s == '18':  # chuvisco
        nuv = 'BKN'
        tp = 'DZ'
        vis = '5000'
    return nuv,tp,vis,nuvcb

#arqi=pd.read_csv('estacaomodeloicon.csv', encoding='iso-8859-1', delimiter =';')




#link='https://www.windy.com/-22.910/-43.163/meteogram?-22.935,-43.163,13,m:c0YaeXe' #meteograma
def baixarmodeloNovoprojeto(estacao):
        
        
        



       # driver = webdriver.Firefox()
        # self.driver.set_window_size(1120, 550)

        print('chegou aqui 4444')
        chrome_options = Options()
        print('chegou aqui 5')
        chrome_options.add_argument("--headless")
         
        print('chegou aqui 666')
        browser = webdriver.Chrome(options=chrome_options)
        browser = get_driver()
        wait = WebDriverWait(browser, 20)
        print('chegou aqui 7')
        #for no in range(0, len(arqi), 1):
        for jj in range(0,1,1):
            try:

                if jj==0:
                    arqi = pd.read_csv('estacaomodeloecmwf.csv', encoding='iso-8859-1', delimiter=';')
                else:
                    arqi = pd.read_csv('estacaomodeloicon.csv', encoding='iso-8859-1', delimiter=';')
                arqi = arqi.loc[(arqi['estacao'] == estacao.upper())]
                arqi = arqi.reset_index(drop=True)

                for no in range(0, 1, 1):

                    link = arqi['endereco'][no]
                    horazulu=arqi['horzulu'][no]
                    print('Loading...')
                    browser.get(link)

                    forecast = {}

                # while True:

                    sleep(12)
                    s = BeautifulSoup(browser.page_source, "html.parser")
                    horagmt=arqi['horzulu'][no]
                    # text_file = open("forecast.txt", "w")
                    # text_file.write(s.find_all('script'))
                    # text_file.close()



                   # rows = s.find("table", {"class": "grab"}).find("tbody").find_all("tr")
                    rows= s.find(id="detail-data-table").find("tbody").find_all("tr")
                    s.find()
                    # rows = s.find("table", {"class": "tabulka"}).find("tbody").find_all("tr", {"id": "tabid_0_0_WINDSPD"})
                    data=[]
                    dataaux=[]
                    hora=[]
                    neb=[]
                    tar=[]
                    prp=[]
                    wspd=[]
                    gust=[]
                    wdir=[]
                    cld=[]
                    vis=[]
                    tp=[]

                    cldcb=[]

                    for i in range(0,8,1): #variável
                        try:
                            #if i==7:
                             #   cc=str(rows[i].contents[i].contents[0])[30:33]
                            #for j in range(0,len)
                            if i==0:
                                for j in range(0,len(rows[0].contents),1):

                                    dataaux.append(datetime.now() + timedelta(days=j))
                                    data.append(rows[i].contents[j].string)


                            else:
                                for j in range(0,len(rows[3].contents),1):

                                    if i==1:
                                        hora.append(rows[i].contents[j].string)
                                    elif i==2:
                                        numv=''
                                        for nuv in str(rows[i].contents[j].contents[0])[29:35]:
                                            if nuv.isdigit():
                                                numv = numv + nuv
                                        neb.append(numv)
                                        nuv,tep,visi,nucb=qnuvem(numv)
                                        cld.append(nuv)
                                        cldcb.append(nucb)
                                        tp.append(tep)
                                        vis.append(visi)
                                    elif i==3:
                                        apenasDigitos = ''

                                        for taraux in rows[i].contents[j].string:
                                            if taraux.isdigit():
                                                apenasDigitos = apenasDigitos + taraux
                                        tar.append(apenasDigitos)
                                        #tar.append(rows[i].contents[j].string)
                                    elif i==4:
                                        prp.append(rows[i].contents[j].string)
                                    elif i==5:
                                        wspd.append(int(rows[i].contents[j].string))
                                    elif i==6:
                                        gust.append(rows[i].contents[j].string)
                                    else:
                                        apenasDigitos =''

                                        for wdiraux in str(rows[i].contents[j].contents[0])[30:33]:
                                            if wdiraux.isdigit():
                                                apenasDigitos=apenasDigitos+wdiraux
                                        wdir.append(apenasDigitos)
                        except:
                            continue

                    print(data)
                    print(hora)
                    print(neb)
                    print(tar)
                    print(prp)
                    print(wspd)
                    print(gust)
                    print(wdir)
                    estacao=[arqi['estacao'][no]]*len(wdir)
                    j=0
                    dd=[]
                    datazulu=[]
                    dateFormatter = "%d/%m/%Y %H:%M"
                    #datetime.strptime(dateString, dateFormatter)
                    for i in range(0,len(hora),1):
                        try:
                            dia=dataaux[j].day
                            mes=dataaux[j].month
                            ano=dataaux[j].year
                            hor=hora[i]
                            d = str(dia) + '/' + str(mes) + '/' + str(ano) + ' ' + hor + ':00'


                            # timedelta(hours=3)
                            # if horagmt !=3:
                            #     if horagmt <3:
                            #         hor=str(int(hor)-(3-horagmt))
                            #     elif horagmt==4:
                            #         hor =str(int(hor)+(1))
                            #     elif horagmt==5:
                            #         hor =str(int(hor)+(2))
                            #
                            #     else:
                            #         hor = str(int(hor) + (horagmt - 3))
                            #
                            #
                            # if horagmt != 3:
                            #     if horagmt < 3:
                            #         if '0' == str(int(hora[i]) - 3 +horagmt) and hor != '3':
                            #             j=j+1
                            #     elif horagmt==4:
                            #         if '0' == str(int(hora[i]) +2 -horagmt)  and hor !='3':
                            #             j=j+1
                            #             if hor=='24':
                            #                 hor='0'
                            #     elif horagmt == 5:
                            #         if '0' == str(int(hora[i]) +4 -horagmt)  and hor !='3':
                            #             j=j+1
                            #             if hor=='24':
                            #                 hor='0'
                            # else:
                            if horazulu == 5:
                                if hora[i] == '19':
                                    j = j + 1
                                if hora[i] == '22':
                                    dia=dia-1
                            elif horazulu == 4:
                                if hora[i] == '20':
                                    j = j + 1
                                if hora[i] == '23':
                                    dia=dia-1

                            elif horazulu == 3:
                                if hora[i] == '21':
                                    j = j + 1
                            elif horazulu == 2:
                                if hora[i] == '22':
                                    j = j + 1
                            #

                            d = str(dia) + '/' + str(mes) + '/' + str(ano) + ' ' + hor + ':00'
                            dd.append(datetime.strptime(d, dateFormatter))
                            datazulu.append(datetime.strptime(d, dateFormatter) + timedelta(hours=int(horazulu)))
                            # fuso_horario = timezone('Greenwich')
                            # data_e_hora_sao_paulo = datetime.strptime(d, dateFormatter).astimezone(fuso_horario)
                            # datazulu.append(data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M'))
                            #
                            # dd.append(datetime.strptime(d, dateFormatter))
                        # for k in range(0,len(neb),1):
                        #     cc = ''
                        #     #print(cc,' ',neb[k])
                        #     cc = cc + 3
                        #     if cc > 24:
                        #         cc=3



                            # cc=rows[i].contents[i].string
                            # print(type(cc))
                            # #forecast[id] = []
                            # #i = 0
                            # for cell in cells:
                            #     if ('DIRPW' in id): # or ('DIRPW' in id):
                            #         print(id + " " + str(i))
                            #         value = cell.find('span').find('svg').find('g')["transform"]
                            #     else:
                            #         value = cell.get_text()
                            #     forecast[id].append(value)
                            #     i = i + 1
                        except:
                            continue
                    lista_de_tuplas = list(zip(estacao,dd, wspd,wdir,gust,tar,prp,neb,cld,cldcb,vis,tp,datazulu))

                    df= pd.DataFrame(
                        lista_de_tuplas,
                        columns=['estacao','datahora', 'wspd', 'wdir', 'gust', 'tar', 'prp', 'neb','cld','cldcb','vis','tp','datazulu']
                    )
                    print(forecast)
                    if no!=0:
                        df1=pd.concat([df,df1])
                    else:
                        df1=df
                df1 = df1.reset_index(drop=True)

                if datetime.now().day<10:
                    diaf='0'+str(datetime.now().day)
                else:
                    diaf = str(datetime.now().day)

                if datetime.now().month<10:
                    mesf='0'+str(datetime.now().month)
                else:
                    mesf = str(datetime.now().month)

                if jj==0:
                    nomearq = 'dadosecmwf_area' + str(area) + '_' + diaf + mesf + '.csv'
                else:
                    nomearq = 'dadosicon_area' + str(area) + '_' + diaf + mesf + '.csv'
                df1.to_csv(nomearq)#, encoding='utf-8', index=False, date_format='%d/%m/%Y %H:%M')
            except:
                continue
        driver.quit()
        return link,df1,horazulu


def lookup_coord(city_name,usu):
    """Function to lookup the names of city"""
    print('chegou aqui')
    if usu==1:
        df = pd.read_csv("cities_transformed3.csv")
    else:
        df = pd.read_csv("cities_transformed3.csv")
    city_data = df[df['city'].str.lower() == city_name]
    if not city_data.empty:

        lat = city_data['lat'].iloc[0]
        lon = city_data['lon'].iloc[0]
        return lat, lon
    else:
        return None


def sort_data(weather_data):
    """"Function to extract data from json"""

    extracted_data = []
    for i in range(len(weather_data)):
        date, time = (weather_data['datazulu'][i]).strftime('%d/%m/%Y %H:%M').split(' ')
        #date, time = weather_data.datazulu[i].split(' ')

        temp = weather_data['tar'][i]
        #feel_temp = weather_data['list'][i]['main']['feels_like']
        #min_temp = weather_data['list'][i]['main']['temp_min']
        #max_temp = weather_data['list'][i]['main']['temp_max']
        #pressure = weather_data['list'][i]['main']['pressure']
        #sea_level = weather_data['list'][i]['main']['sea_level']
        #grnd_level = weather_data['list'][i]['main']['grnd_level']
        #humidity = weather_data['list'][i]['main']['humidity']
        wspd=weather_data['wspd'][i]
        wdir=weather_data['wdir'][i]
        gust=weather_data['gust'][i]
        visibilidade=weather_data['vis'][i]
        if visibilidade=='9999':
            visibilidade='10000'

        chuva=weather_data['prp'][i]
        td=(weather_data['tdr'][i])
        ur= str(round(100 - 5 * (int(temp) - int(td))))
        nbaixas=str(weather_data['nbaixa'][i])
        if nbaixas[-1]=='k':
            nbaixas=str(int(nbaixas[0:len(nbaixas)-1])*3281)
        elif nbaixas=='--':
            nbaixas = 'Nil'
        else:
            nbaixas=str(int(int((nbaixas))*3.281))
        if len(nbaixas)>5:
            nbaixas=nbaixas[0:5]

        tp=weather_data['tp'][i]
        if tp=='':
            tp='Nil'
        cld=weather_data['cld'][i]
        cldcb=weather_data['cldcb'][i]
        pressao=(weather_data['pressao'][i])
        #weather_status = weather_data['list'][i]['weather'][0]['main']
        extracted_data.append(
            (weather_data['estacao'][i], date, time, temp,ur,pressao,
             tp, cld, cldcb,wspd,wdir,gust,visibilidade,nbaixas))

    # push_data(extracted_data)
    return extracted_data


def authenticate(city):

    """Function to request information from OpenWeatherMap API giving the necessary details"""
    #try:

    print('chegou aqui 2')


    link,data,horazulu=baixarmodeloNovoprojeto(city)
    data1=baixaamodeloNovometeograma.Scraper(city,link,horazulu)

    print('chegou aqui 3')

    #except Exception as e:
    #    st.error(f"Could not get the data because {e}. Exiting...")
    #    st.stop()
    #data = pd.read_csv("dadosecmwf_area2_1104.csv")
    data=pd.merge(data, data1, how='inner', on='datahora')
    data=data.drop(['tar_y', 'estacao_y', 'datazulu_y'], 1)
    data=data.rename(columns={'estacao_x': 'estacao', 'tar_x': 'tar', 'datazulu_x': 'datazulu'})


    return data
