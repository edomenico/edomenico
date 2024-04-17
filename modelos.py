import backend

from streamlit import runtime
import sys
from streamlit.web import cli as stcli
import streamlit as st
import pandas as pd
import plotly.express as px
import novo_projeto2
def main():
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
            import re
            import urllib.parse
            import pandas as pd
            from selenium import webdriver
            from bs4 import BeautifulSoup
            from time import sleep
            from datetime import datetime,timedelta
            from datetime import date
            from pytz import timezone
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.wait import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            
            from selenium.common.exceptions import TimeoutException
            from selenium.webdriver.common.by import By
            from selenium.webdriver.firefox.options import Options
            from selenium.webdriver.firefox.service import Service
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.support.ui import WebDriverWait
            from webdriver_manager.firefox import GeckoDriverManager
    
    
    
    
           # driver = webdriver.Firefox()
            # self.driver.set_window_size(1120, 550)
    
    
            options = Options()
            options.add_argument('--disable-gpu')
            options.add_argument('--headless')
        
    
    
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            
                # Create the driver with the options
            driver = webdriver.Chrome(options=chrome_options)
            #firefoxOptions = Options()
            #firefoxOptions.add_argument("--headless")
            #service = Service(GeckoDriverManager().install())
            #driver = webdriver.Firefox(
            #options=firefoxOptions,
            #service=service,
            #)
            #for no in range(0, len(arqi), 1):
            for jj in range(0,1,1):
                try:
    
                    if jj==0:
                        arqi = pd.read_csv('estacaomodeloecmwf.csv', encoding='iso-8859-1', delimiter=';')
                    else:
                        arqi = pd.read_csv('estacaomodeloicon.csv', encoding='iso-8859-1', delimiter=';')
                    arqi = arqi.loc[(arqi['estacao'] == estacao.upper())]
                    arqi = arqi.reset_index(drop=True)
                    print('chegou aqui b222')
                    for no in range(0, 1, 1):
    
                        link = (arqi['endereco'][no])
                        print(link)
                        horazulu=arqi['horzulu'][no]
                        print(horazulu)
                        link='https://www.windy.com/-22.989/-43.375?-23.132,-43.375,10,i:pressure,m:c0QaeWR'
                        #driver = get_driver()
                        driver.get(link)
                        wait = WebDriverWait(driver, 20)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))
                        print('chegou aqui b33')
    
                        forecast = {}
    
                    # while True:
    
                       
                        s = BeautifulSoup(driver.page_source, "html.parser")
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
                        print('chegou aqui baixarmodeloNovoprojeto')
                        print (df)
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
    
    def baixaamodeloNovometeograma(estacao,link,horazulu):
            import re
            import urllib.parse
            import pandas as pd
            from selenium import webdriver
            from bs4 import BeautifulSoup
            from time import sleep
            from datetime import datetime,timedelta
            from datetime import date
            from pytz import timezone
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.wait import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            
            from selenium.common.exceptions import TimeoutException
            from selenium.webdriver.common.by import By
            from selenium.webdriver.firefox.options import Options
            from selenium.webdriver.firefox.service import Service
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.support.ui import WebDriverWait
            from webdriver_manager.firefox import GeckoDriverManager
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            
                # Create the driver with the options
            driver = webdriver.Chrome(options=chrome_options)
            
            print('chegou aqui b1')
    
            for jj in range(0,1,1):
                try:
    
                    # if jj==0:
                    #     arqi = pd.read_csv('estacaomodeloecmwf.csv', encoding='iso-8859-1', delimiter=';')
                    # else:
                    #     #arqi = pd.read_csv('estacaomodeloicon.csv', encoding='iso-8859-1', delimiter=';')
                    #arqi = arqi.loc[(arqi['area'] == area)]
                    #arqi = arqi.reset_index(drop=True)
    
                    for no in range(0, 1, 1):
    
                        #link = arqi['endereco'][no]
                        posicaoi=str.find(link,"?")
                        posicaof=str.find(link,"pressure")+8
                        link1=link[0:posicaoi] + '/meteogram' + link[posicaoi:posicaof]
                        #link='https://www.windy.com/-22.810/-43.253/meteogram?-23.020,-43.253,10,i:pressure'
                        #horazulu=3
                        print('Loading...')
                        print('chegou aqui bm2223')
                        print(link1)
                        link1='https://www.windy.com/-22.989/-43.375/meteogram?-23.187,-43.375,10,i:pressure'
                        
                        driver.get(link1)
                        wait = WebDriverWait(driver, 20)
                        wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))
                        print('chegou aqui b33')
                        html = driver.page_source
                        forecast = {}
    
                    # while True:
    
                        
                        print('chegou aqui b4')
                        s = BeautifulSoup(html, "html.parser")
                        print('chegou aqui b5')
                       # horagmt=arqi['horzulu'][no]
                        # text_file = open("forecast.txt", "w")
                        # text_file.write(s.find_all('script'))
                        # text_file.close()
    
    
    
                       # rows = s.find("table", {"class": "grab"}).find("tbody").find_all("tr")
                        rows= s.find(id="detail-data-table").find("tbody").find_all("tr")
                        print('chegou aqui b6')
                        s.find()
                        # rows = s.find("table", {"class": "tabulka"}).find("tbody").find_all("tr", {"id": "tabid_0_0_WINDSPD"})
                        data=[]
                        dataaux=[]
                        hora=[]
    
                        tar=[]
                        tdr=[]
                        nbaixa=[]
    
                        pressao=[]
    
    
    
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
    
                                        elif i==3:
    
    
    
                                            apenasDigitos1 = rows[i].contents[j].text[0:2]
                                            apenasDigitos2 = rows[i].contents[j].text[3:5]
                                            tar.append(apenasDigitos1)
                                            tdr.append(apenasDigitos2)
                                            #tar.append(rows[i].contents[j].string)
    
                                        elif i==5:
                                            pressao.append(rows[i].contents[j].string)
                                        elif i==7:
                                            nbaixa.append(rows[i].contents[j].string)
    
                            except:
                                continue
    
    
                        #estacao='SBGL'*len(tar)
                        estacao=[estacao.upper() for x in range(len(tar))]
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
                        lista_de_tuplas = list(zip(estacao,dd,tar,tdr,pressao,nbaixa,datazulu))
    
                        df= pd.DataFrame(
                            lista_de_tuplas,
                            columns=['estacao','datahora', 'tar', 'tdr', 'pressao','nbaixa','datazulu']
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
    
                    # if jj==0:
                    #     nomearq = 'dadosecmwf_area_o' +  '_' + diaf + mesf + '.csv'
                    # else:
                    #     nomearq = 'dadosicon_area' + '_' + diaf + mesf + '.csv'
                    # df1.to_csv(nomearq)#, encoding='utf-8', index=False, date_format='%d/%m/%Y %H:%M')
                except:
                    continue
            driver.quit()
            return df1
    
    
    def lookup_coord2(city_name,usu):
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
    
    
    def sort_data2(weather_data):
        """"Function to extract data from json"""
        print('extracted')
        print(weather_data)
        
    
        extracted_data = []
        for i in range(len(weather_data)):
            date, time = (weather_data['datazulu'][i]).strftime('%d/%m/%Y %H:%M').split(' ')
            #date, time = weather_data.datazulu[i].split(' ')
    
            temp = weather_data['tar'][i]
            print(temp)
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
    
    
    def authenticate2(city):
    
        """Function to request information from OpenWeatherMap API giving the necessary details"""
        #try:
    
        print('chegou aqui 2')
    
    
        link,data1,horazulu=baixarmodeloNovoprojeto(city)
       # city='SBJR'
       # link='https://www.windy.com/-22.910/-43.163/meteogram?-22.935,-43.163,13,m:c0YaeXe'
       # horazulu=3
        print('chegou aqui 333333333')
        print (data1)
        data2=baixaamodeloNovometeograma(city,link,horazulu)
        print('chegou aqui 2222222222222')
       
    
        #except Exception as e:
        #    st.error(f"Could not get the data because {e}. Exiting...")
        #    st.stop()
        #data = pd.read_csv("dadosecmwf_area2_1104.csv")
        data3=pd.merge(data1, data2, how='inner', on='datahora')
        print(data3)
        print('chegou aqui 44444444444444')
        #data1=data.drop(['tar_y', 'estacao_y', 'datazulu_y'], axis=1)
        print('chegou aqui 5555555555555')
        
        data4=data3.rename(columns={'estacao_x': 'estacao', 'tar_x': 'tar', 'datazulu_x': 'datazulu'})
        print('chegou aqui 66666666666666')
        print(data4)
    
    
        return data4
    
    def search2(city,usu):
        try:
            lat, lon = lookup_coord2(city,usu)
                # st.write(lat)
            print('novo_projeto 1')
            data = authenticate2(city)
                # st.write(data)
            print('novo_projeto 2')
            print(data)
            extracted_data = sort_data2(data)
                # st.write(extracted_data)
            return extracted_data, lat, lon
        except Exception as e:
            print(f"Cannot locate this city. Reason: {e}")
    
    
    
    
    def temp_time_series2(df):
        """Container for temperature time series"""
        temp_time_df = pd.DataFrame(
            {'temp': df['temp'], 'ur': df['ur'],'timestamp': df['timestamp']})
        fig = px.line(temp_time_df, x='timestamp', y=['temp', 'ur'],
                      title='Temperatura(°C) e Umidade Relativa(%)')
        fig.update_yaxes(title="Valor")
            #fig.update_xaxes(title="dia")
        new = {'temp': 'Temperatura Atual(°C)', 'ur': 'Umidade (%)'}
        fig.for_each_trace(lambda t: t.update(name=new[t.name]))
            # fig.update_legends(selector={'actual_temp': 'Air Temperature'})
            # fig = px.scatter(title='Temp')
            # fig.add_scatter(x=df['timestamp'], y=df['actual_temp'],mode='lines',name='Actual Temperature')
            # fig.add_scatter(x=df['timestamp'], y=df['feels_like_temp'],mode='lines',name='Feels-like Temperature')
            # fig.update_xaxes(title="Date", tickformat="%d-%m-%Y")
            # fig.update_yaxes(title="Temperature (°C)", range=[df['min_temp'].min(), df['max_temp'].max()])
        st.plotly_chart(fig, use_container_width=True)
    
    
    def weather_pie2(df):
        """Container for pie chart of weather conditions"""
        labels = list(set(df['tp']))
        values = [sum([i == j for i in df['tp']]) for j in labels]
        fig = px.pie(values=values, labels=labels, title="Condições do tempo", hover_name=labels, names=labels)
        st.plotly_chart(fig, use_container_width=True)
    
    
    def min_max2(df):
        """Container for minimum and maximum temperatures"""
            # min_max_df = pd.DataFrame({'max_temp': df.groupby('date')['max_temp'].max(), 'date': df['date'].unique(), 'min_temp':df.groupby('date')['min_temp'].min()})
            # fig = px.line(min_max_df, x= 'date', y=['max_temp','min_temp'],title='Minimum and Maximum Temperature')
            # new = {'max_temp':'Maximum Temperature', 'min_temp': 'Minimum Temperature'}
            # fig.for_each_trace(lambda t: t.update(name = new[t.name]))
        ####df['data'].unique()[0:len(df['data'].unique()) - 1]
        #####df.groupby('data')['temp'].max()[0:len(df['data'].unique()) - 1]
        fig = px.scatter(title='Temperatura máxima e mínima')
        fig.add_scatter(x=df['data'].unique()[0:len(df['data'].unique()) - 1], y=df.groupby('data')['temp'].max()[0:len(df['data'].unique()) - 1], name='Temperatura Máxima')
        fig.add_scatter(x=df['data'].unique()[0:len(df['data'].unique()) - 1], y=df.groupby('data')['temp'].min()[0:len(df['data'].unique()) - 1], name='Temperatura Mínima')
        fig.update_yaxes(title="Temperatura (°C)")
        st.plotly_chart(fig, use_container_width=True)
    
    
    def vento2(df):
        """Container for temperature time series"""
            # vento_df = pd.DataFrame(
            #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})
    
        fig = px.scatter(title='Vento')
        fig.add_scatter(x=df['timestamp'], y=df['int vento'], name='Int.vento(kt)')
        fig.add_scatter(x=df['timestamp'], y=df['dir vento'], name='Dir.vento(graus)')
        fig.update_yaxes(title="Valor")
        st.plotly_chart(fig, use_container_width=True)


    def search(city,usu):
        try:
            lat, lon = backend.lookup_coord(city,usu)
            # st.write(lat)
            data = backend.authenticate(lat, lon)
            # st.write(data)
            extracted_data = backend.sort_data(data)
            # st.write(extracted_data)
            return extracted_data, lat, lon
        except Exception as e:
            print(f"Cannot locate this city. Reason: {e}")


    def emoji(emoji):
        weather_emoji = {
            'Clouds': ':cloud:',
            'Clear': ':sun_behind_cloud:',
            'Rain': ':rain_cloud:',
            'Snow': ':snowflake:'
        }
        if emoji in weather_emoji:
            return weather_emoji[emoji]
        else:
            return ''


    def temp_time_series():
        """Container for temperature time series"""
        temp_time_df = pd.DataFrame(
            {'temp': df['temp'], 'sens.term': df['sens.term'], 'timestamp': df['timestamp']})
        fig = px.line(temp_time_df, x='timestamp', y=['temp', 'sens.term'],
                      title='Temperatura e Sensação térmica')
        fig.update_yaxes(title="Temperatura (°C)")
        fig.update_xaxes(title="dia")
        new = {'temp': 'Temperatura Atual', 'sens.term': 'Sensação Térmica'}
        fig.for_each_trace(lambda t: t.update(name=new[t.name]))
        # fig.update_legends(selector={'actual_temp': 'Air Temperature'})
        # fig = px.scatter(title='Temp')
        # fig.add_scatter(x=df['timestamp'], y=df['actual_temp'],mode='lines',name='Actual Temperature')
        # fig.add_scatter(x=df['timestamp'], y=df['feels_like_temp'],mode='lines',name='Feels-like Temperature')
        # fig.update_xaxes(title="Date", tickformat="%d-%m-%Y")
        # fig.update_yaxes(title="Temperature (°C)", range=[df['min_temp'].min(), df['max_temp'].max()])
        st.plotly_chart(fig, use_container_width=True)


    def weather_pie():
        """Container for pie chart of weather conditions"""
        labels = list(set(df['tempo']))
        values = [sum([i == j for i in df['tempo']]) for j in labels]
        fig = px.pie(values=values, labels=labels, title="Condições do tempo", hover_name=labels, names=labels)
        st.plotly_chart(fig, use_container_width=True)


    def min_max():
        """Container for minimum and maximum temperatures"""
        # min_max_df = pd.DataFrame({'max_temp': df.groupby('date')['max_temp'].max(), 'date': df['date'].unique(), 'min_temp':df.groupby('date')['min_temp'].min()})
        # fig = px.line(min_max_df, x= 'date', y=['max_temp','min_temp'],title='Minimum and Maximum Temperature')
        # new = {'max_temp':'Maximum Temperature', 'min_temp': 'Minimum Temperature'}
        # fig.for_each_trace(lambda t: t.update(name = new[t.name]))

        fig = px.scatter(title='Temperatura máxima e mínima')
        fig.add_scatter(x=df['data'].unique(), y=df.groupby('data')['temp_max'].max(), name='Temperatura Máxima')
        fig.add_scatter(x=df['data'].unique(), y=df.groupby('data')['temp_min'].min(), name='Temperatura Mínima')
        fig.update_yaxes(title="Temperatura (°C)")
        st.plotly_chart(fig, use_container_width=True)


    def vento():
        """Container for temperature time series"""
        vento_df = pd.DataFrame(
            {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})
        fig = px.line(vento_df, x='timestamp', y=['dir.vento', 'int.vento'],
                      title='Vento')
        new = {'dir.vento': 'Direção do vento(graus)', 'int.vento': 'Intensidade do vento(kt)'}
        fig.for_each_trace(lambda t: t.update(name=new[t.name]))
        fig.update_xaxes(title="dia")
        fig.update_yaxes(title="valor")
        # fig.update_legends(selector={'actual_temp': 'Air Temperature'})
        # fig = px.scatter(title='Temp')
        # fig.add_scatter(x=df['timestamp'], y=df['actual_temp'],mode='lines',name='Actual Temperature')
        # fig.add_scatter(x=df['timestamp'], y=df['feels_like_temp'],mode='lines',name='Feels-like Temperature')
        # fig.update_xaxes(title="Date", tickformat="%d-%m-%Y")
        # fig.update_yaxes(title="Temperature (°C)", range=[df['min_temp'].min(), df['max_temp'].max()])
        st.plotly_chart(fig, use_container_width=True)


    st.set_page_config(page_title='Previsão', page_icon='	:satellite:', layout='wide',
                       initial_sidebar_state='expanded')

    # Page header
    st.title("App Previsão Tempo:satellite:")
    st.text('Previsão para 5 dias.')
    st.divider()
    area_escolhida =['SBJR', 'SBES', 'SBME', 'SBCP', 'SBFS','SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS',
                            'SBAC','SBJE', 'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU',
                            'SBKG', 'SBFN','SBPL', 'SBPJ','SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA',
                           'SBCJ','SBHT', 'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBMY',
                            'SBTF', 'SBUA','SBEG', 'SBBV', 'SSKW', 'SWEI', 'SWPI']

    with st.sidebar.container():
        modelo = st.radio("Escolha o modelo", ["OpenWeather", "ECMWF", "ICON(em construção)"])

        if modelo=="OpenWeather":

            usuario = st.radio("Escolha o usuário", ["Previsor(CMA-GL)", "Público Geral"])
            if usuario == 'Previsor(CMA-GL)':
                city = st.selectbox('**Selecione o aeródromo**', area_escolhida).lower()
                #city = st.sidebar.text_input('**Aeródromo(ICAO)**' , placeholder=' ').lower()
                usu=1
                button =city
            else:
                city = st.sidebar.text_input('**Nome da cidade**' , placeholder=' ').lower()
                usu=2
                button = st.sidebar.button('Procura')
        elif modelo=="ECMWF":
            city = st.selectbox('**Selecione o aeródromo**', area_escolhida).lower()
            # city = st.sidebar.text_input('**Aeródromo(ICAO)**' , placeholder=' ').lower()
            usu = 1
            button = city


        #city = st.sidebar.text_input('**Nome da cidade** , placeholder=' ').lower()
        #button = st.sidebar.button('Procura :microscope:')

        #units = st.sidebar.radio("##Select temperature units: ", ["Celsius", "Fahrenheit", "Kelvin"],
        #                         label_visibility='collapsed')
        st.sidebar.divider()



       # st.sidebar.divider()


        show_map = st.sidebar.checkbox('Mostrar mapa')
    if modelo=="OpenWeather":
        if button or city:
            if not city:
                pass
            result, lat, lon = search(city,usu)
            # st.write(result)
            df = pd.DataFrame(result)
            df.rename(
                columns={0: 'cidade', 1: 'país', 2: 'data', 3: 'hora', 4: 'temp', 5: 'sens.term', 6: 'temp_min',
                         7: 'temp_max',
                         8: 'pressão', 9: 'sea_level', 10: 'grnd_level', 11: 'umidade', 12: 'tempo', 13: 'int vento', 14: 'dir vento', 15: 'raj vento', 16: 'visibilidade'}, inplace=True)
            df['timestamp'] = (df['data'] + ' ' + df['hora'])
            # if units == 'Celsius':
            #     df['temp'] = df['temp'] - 273.15
            #     df['sens.term'] = df['sens.term'] - 273.15
            #     df['temp_max'] = df['temp_max'] - 273.15
            #     df['temp_min'] = df['temp_min'] - 273.15
            #
            # elif units == 'Fahrenheit':
            #     df['temp'] = df['temp'] * 9 / 5 - 459.67
            #     df['sens.term'] = df['sens.term'] * 9 / 5 - 459.67
            #     df['temp_max'] = df['temp_max'] * 9 / 5 - 459.67
            #     df['temp_min'] = df['temp_min'] * 9 / 5 - 459.67
            #
            # else:
            #     pass

            with st.container():

                st.header(f"{city.capitalize().upper()}, {df['país'].iloc[0]} {emoji(df['tempo'].iloc[0])}")
                st.subheader(str(df['timestamp'].iloc[0])[0:16]+'UTC')
                col1, col2, col3 = st.columns(3)
                with col1:
                    col1.metric("Temperatura(°C)", f"{round(df['temp'].iloc[0], 1)}")
                    col1.metric("Umidade(%)", f"{df['umidade'].iloc[0]}")
                with col2:
                    col2.metric("Sensação Térmica(°C)", f"{round(df['sens.term'].iloc[0], 1)}")
                    col2.metric("Pressão (hPa)", f"{df['pressão'].iloc[0]}")
                with col3:
                    col3.metric("Tempo", f"{df['tempo'].iloc[0]}")
                    col3.metric("Vento(graus/kt)",  f"{round(df['dir vento'].iloc[0], 0)} / {int(df['int vento'].iloc[0])}")

                st.divider()
                with st.container():

                    col1, col2 = st.columns((5, 5))
                    with col1:
                        temp_time_series()
                    with col2:
                        weather_pie()

                    col3, col4 = st.columns((5, 5))
                    with col3:
                        min_max()
                    with col4:
                        vento()

                if show_map and city:
                    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), use_container_width=True)

                st.divider()

                with st.expander(label="Mostrar dados:"):
                    st.table(df)
    elif modelo=="ECMWF":


        #usuario = st.radio("Escolha o usuário", ["Previsor(CMA-GL)", "Público Geral"], disabled=True,on_change='hidden')


        if button or city:
            if not city:
                pass
            
            result, lat, lon = search2(city, usu)
            print(result)
            print('modelos p1')
            # st.write(result)
            df = pd.DataFrame(result)
            df1 = pd.DataFrame(result)
            print(df)
            print('modelos p2')
            df.rename(
                columns={0: 'estacao', 1: 'data', 2: 'hora', 3: 'temp', 4: 'ur', 5: 'pressao', 6: 'tp',
                         7: 'ceu',8: 'ncb',9: 'int vento',
                         10: 'dir vento', 11: 'raj vento', 12: 'visibilidade', 13: 'nbaixas'}, inplace=True)



            print('modelos p3')
            df['timestamp'] = (df['data'] + ' ' + df['hora'])
            print('modelos p4')
            # if units == 'Celsius':
            #     df['temp'] = df['temp'] - 273.15
            #     df['sens.term'] = df['sens.term'] - 273.15
            #     df['temp_max'] = df['temp_max'] - 273.15
            #     df['temp_min'] = df['temp_min'] - 273.15
            #
            # elif units == 'Fahrenheit':
            #     df['temp'] = df['temp'] * 9 / 5 - 459.67
            #     df['sens.term'] = df['sens.term'] * 9 / 5 - 459.67
            #     df['temp_max'] = df['temp_max'] * 9 / 5 - 459.67
            #     df['temp_min'] = df['temp_min'] * 9 / 5 - 459.67
            #
            # else:
            #     pass

            with st.container():
                stp = ""

                st.header(f"{city.capitalize().upper()}, BR {emoji(df['tp'].iloc[0])}")
                st.subheader(str(df['timestamp'].iloc[0])[0:16] + 'UTC')
                col1, col2, col3 = st.columns(3)
                with col1:
                    col1.metric("Temperatura(°C)", f"{(df['temp'].iloc[0])}")
                    if df['ceu'].iloc[0] == 'FEW':
                        sceu = 'Poucas nuvens'
                    elif df['ceu'].iloc[0] == 'SCT':
                        sceu = 'Parcialmente nublado'
                    elif df['ceu'].iloc[0] == 'BKN':
                        sceu = 'Nublado'
                    elif df['ceu'].iloc[0] == 'OVC':
                        sceu = 'Encoberto'
                    else:
                        sceu = 'Claro'

                    # col1.metric("Céu", f"{df['ceu'].iloc[0]}")
                    col1.metric("Céu", sceu)
                    col1.metric("Umidade", f"{df['ur'].iloc[0]}")

                with col2:
                    if df['tp'].iloc[0] == 'BR':
                        stp = 'Névoa'
                    elif df['tp'].iloc[0] == 'RA':
                        stp = 'Chuva'
                    elif df['tp'].iloc[0] == 'TS':
                        stp = 'Trovoada'
                    elif df['tp'].iloc[0] == 'TSRA':
                        stp = 'Trovoada com chuva'
                    else:
                        stp = 'Nil'
                    # col2.metric("Tempo presente", f"{(df['tp'].iloc[0])}")
                    col2.metric("Tempo presente", stp)
                    col2.metric("Visibilidade(m)", f"{df['visibilidade'].iloc[0]}")
                    col2.metric("Pressão(hPa)", f"{df['pressao'].iloc[0]}")
                with col3:
                    # col3.metric("Tempo", f"{df['tp'].iloc[0]}")
                    col3.metric("Rajada(kt)", f"{(df['raj vento'].iloc[0])}")
                    col3.metric("Vento(graus/kt)", f"{(df['dir vento'].iloc[0])} / {int(df['int vento'].iloc[0])}")
                    col3.metric("Altura nuvens baixas(ft)", f"{df['nbaixas'].iloc[0]}")

                st.divider()
                with st.container():

                    col1, col2 = st.columns((5, 5))
                    with col1:
                        
                        temp_time_series2(df)
                    with col2:
                        
                        weather_pie2(df)

                    col3, col4 = st.columns((5, 5))
                    with col3:
                        
                        min_max2(df)
                    with col4:
                        vento2(df)

                if show_map and city:
                    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), use_container_width=True)

                st.divider()

                with st.expander(label="Mostrar dados:"):
                    st.table(df)

main()
