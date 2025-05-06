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
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager
            from webdriver_manager.core.os_manager import ChromeType
            import time

    
            def get_driver():
                return webdriver.Chrome(
                    service=Service(
                        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
                    ),
                    options=options,
                )
        
            options = Options()
            options.add_argument("--disable-gpu")
            options.add_argument("--headless")
            print('cheguei aqui 1')
            driver = get_driver(options=chrome_options)
            print('cheguei aqui 2')
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
                    print('baixarmodeloNovoprojeto 2')
                    
                    arqi = arqi.reset_index(drop=True)
                    print(arqi)
                    for no in range(0, 1, 1):
    
                        link = (arqi['endereco'][no])
                        
                        horazulu=arqi['horzulu'][no]
                        #horazulu='3'
                        
                        
                        #link='https://www.windy.com/-22.989/-43.375?-23.132,-43.375,10,i:pressure,m:c0QaeWR'
                        #driver = get_driver()
                        print('cheguei aqui 3')
                        print(link)
                        driver.get(link)
                        print('cheguei aqui 4')
                       # wait = WebDriverWait(driver, 30)
                        #wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))
                        #wait.until(EC.presence_of_element_located((By.ID, "detail-data-table")))
                        #WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, "leaflet-pane leaflet-map-pane")))
                        
                        forecast = {}
    
                    # while True:
    
                       
                        s = BeautifulSoup(driver.page_source, "html.parser")
                        print('cheguei aqui 5')
                        
                        horagmt=arqi['horzulu'][no]
                        
                        # text_file = open("forecast.txt", "w")
                        # text_file.write(s.find_all('script'))
                        # text_file.close()
    
    
    
                       # rows = s.find("table", {"class": "grab"}).find("tbody").find_all("tr")
                       
                        #rows= s.find(id="detail-data-table").find("tbody").find_all("tr")
                        rows = WebDriverWait(driver=driver, timeout=10).until(lambda s: s.find(id="detail-data-table").find("tbody").find_all("tr"))
                        print('cheguei aqui 6')
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
                        print('baixarmodeloNovoprojeto 2222')
                        for i in range(0,8,1): #variável
                            try:
                                #if i==7:
                                 #   cc=str(rows[i].contents[i].contents[0])[30:33]
                                #for j in range(0,len)
                                if i==0:
                                    for j in range(0,len(rows[0].contents),1):
                                        print('baixarmodelo 0000')
                                        #print(rows[0].contents[0])
                                        ddd=str(rows[0].contents[0])[55:65]
                                        print(ddd)
                                        
                                        
                                        dataaux.append(datetime.now() + timedelta(days=j))
                                        data.append(rows[i].contents[j].string)
                                        print((rows[i].contents[j].string))
                                        print('baixarmodelo 1111')
                                        #print(rows[1].contents[0])
                                        
                                        hhh=(str(rows[1].contents[0])[28:29])
                                        #print(hhh)
                                        if hhh=='0':
                                            hhh='00'
                                        #hhhh=(str(rows[1].contents[0])[36:38])
                                        
                                        
                                        #if hhhh=='PM':
                                          #  hhh=str(int(hhh)+12)
                                        
    
    
                                else:
                                    for j in range(0,len(rows[3].contents),1):
    
                                        if i==1:
                                            
                                           
                                            hhh=(str(rows[1].contents[0])[28:30])
                                            
                                            
                                            
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
                                            print('baixarmodeloNovoprojeto 3333')
                                            
                                        elif i==3:
                                            apenasDigitos = ''
    
                                            for taraux in str(rows[i].contents[j]):
                                                b = re.sub('[^0-9]', '', str(rows[i].contents[j]))
                                                #if taraux.isdigit():
                                                    #apenasDigitos = apenasDigitos + taraux
                                            bb= (int(b) - 32) * 5/9
                                            tar.append(str(int(bb)))
                                            print('baixarmodeloNovoprojeto 4444')
                                            
                                                
                                            #tar.append(rows[i].contents[j].string)
                                        elif i==4:
                                            prp.append((rows[i].contents[j].string))
                                            print('baixarmodeloNovoprojeto 5555')
                                           
                                        elif i==5:
                                            wspd.append(int(rows[i].contents[j].string))
                                            print('baixarmodeloNovoprojeto 6666')
                                           
                                        elif i==6:
                                            gust.append(rows[i].contents[j].string)
                                            print('baixarmodeloNovoprojeto 7777')
                                           
                                        else:
                                            print('baixarmodeloNovoprojeto 8888')
                                            apenasDigitos =''
    
                                            for wdiraux in str(rows[i].contents[j].contents[0])[3:35]:
                                                if wdiraux.isdigit():
                                                    b = re.sub('[^0-9]', '', str(rows[i].contents[j].contents[0])[3:35])
                                                    #apenasDigitos=apenasDigitos+wdiraux
                                                    
                                            wdir.append(int(b))
                            except:
                                continue
    
                        print('baixarmodeloNovoprojeto 9999')
                        estacao=[arqi['estacao'][no]]*len(wdir)
                        print (hhh)
                        #for i in range(0,len(estacao),1):
                        print(hhh)
                        if hhh=='0<':
                            hhh='00'
                        elif hhh=='1<':
                            hhh='01'
                        elif hhh=='2<':
                            hhh='02'
                        elif hhh=='3<':
                            hhh='03'
                        elif hhh=='4<':
                            hhh='04'
                        elif hhh=='5<':
                            hhh='05'
                        elif hhh=='6<':
                            hhh='06'
                        elif hhh=='7<':
                            hhh='07'
                        elif hhh=='8<':
                            hhh='08'
                        elif hhh=='9<':
                            hhh='09'
                        
                        datahora1=ddd +" "+hhh+":00"
                        
                        print(datahora1)
                        
                            
                        
                       
                        dia=datahora1[8:10]
                        mes=datahora1[5:7]
                        ano=datahora1[0:4]
                        hor=datahora1[11:16]
                        d = str(dia) + '/' + str(mes) + '/' + str(ano) + ' ' + hor 
                        print('baixarmodeloNovoprojeto 10000')
                       
                        dateFormatter = "%d/%m/%Y %H:%M"
                        d=datetime.strptime(d, dateFormatter)
                        d=d+timedelta(hours=int(horazulu))
                        
                        
                        j=0
                        dd=[]
                        datazulu=[]
                        
                       
                        #datetime.strptime(dateString, dateFormatter)
                        for i in range(0,len(estacao),1):
                            try:
                                print('baixarmodeloNovoprojeto 7777')
                                dd.append(d)
                                datazulu.append(d)
                                #timestring = datetime.strptime((dada + timedelta(hours=3)), dateFormatter)
                                d=d+timedelta(hours=3)
                              
                               # dd.append(datetime.strptime(d, dateFormatter))
                               # datazulu.append(datetime.strptime(dddd, dateFormatter) + timedelta(hours=int(horazulu)))
                                
                                # fuso_horario = timezone('Greenwich')
                                # data_e_hora_sao_paulo = datetime.strptime(d, dateFormatter).astimezone(fuso_horario)
                                # datazulu.append(data_e_hora_sao_paulo.strftime('%d/%m/%Y %H:%M'))
                                #
                                # dd.append(datetime.strptime(d, dateFormatter))
                            
    
    
    
                               
                            except:
                                continue
                        print('baixarmodeloNovoprojeto 8888')
                        lista_de_tuplas = list(zip(estacao,dd, wspd,wdir,gust,tar,prp,neb,cld,cldcb,vis,tp,datazulu))
                       
                        
                        df= pd.DataFrame(
                            lista_de_tuplas,
                            columns=['estacao','datahora', 'wspd', 'wdir', 'gust', 'tar', 'prp', 'neb','cld','cldcb','vis','tp','datazulu']
                        )
                        
                        
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
                    #df1.to_csv(nomearq)#, encoding='utf-8', index=False, date_format='%d/%m/%Y %H:%M')
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
            


        
    
            for jj in range(0,1,1):
                try:
    
                    
    
                    for no in range(0, 1, 1):
    
                        
                        posicaoi=str.find(link,"?")
                        posicaof=str.find(link,"pressure")+8
                        link1=link[0:posicaoi] + '/meteogram' + link[posicaoi:posicaof]
                        #link='https://www.windy.com/-22.810/-43.253/meteogram?-23.020,-43.253,10,i:pressure'
                        #horazulu='3'
                        print('Loading...')
                        
                        #link1='https://www.windy.com/-22.989/-43.375/meteogram?-23.187,-43.375,10,i:pressure'
                        
                        driver.get(link1)
                       # wait = WebDriverWait(driver, 30)
                        #wait.until(EC.presence_of_element_located((By.XPATH, "//body[not(@class='loading')]")))
                        #WebDriverWait(driver,20).until(EC.presence_of_element_located((By.CLASS_NAME, "leaflet-pane leaflet-map-pane")))
                        html = driver.page_source
                        forecast = {}
    
                    # while True:
    
                        
                        
                        s = BeautifulSoup(html, "html.parser")
                        
                       # horagmt=arqi['horzulu'][no]
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
    
                        tar=[]
                        tdr=[]
                        nbaixa=[]
    
                        pressao=[]
    
    
    
                        for i in range(0,8,1): #variável
                            try:
                               
                                if i==0:
                                    for j in range(0,len(rows[0].contents),1):
                                        print('chegou aqui 1')
                                        ddd=str(rows[0].contents[0])[55:65]
                                        dataaux.append(datetime.now() + timedelta(days=j))
                                        data.append(rows[i].contents[j].string)
                                        print (datetime.now() + timedelta(days=j))
                                        print(ddd)
                                        print((str(rows[1].contents[0])))
                                        hhh=(str(rows[1].contents[0])[28:29])
                                        hhhh=(str(rows[1].contents[0])[36:38])
                                        print('chegou aqui 2')
                                        print(hhh)
                                        print(hhhh)
                                        if hhhh=='PM':
                                            hhh=str(int(hhh)+12)
    
    
                                else:
                                    for j in range(0,len(rows[3].contents),1):
    
                                        if i==1:
                                            
                                           
                                            print('chegou aqui 3')
                                            print((str(rows[i].contents[j])))
                                            hhh=(str(rows[1].contents[0])[28:30])
                                            
    
                                        elif i==3:
    
    
                                            
                                             apenasDigitos1 = rows[i].contents[j].text[0:2]
                                             apenasDigitos2 = rows[i].contents[j].text[3:5]
                                             #tar.append(apenasDigitos1)
                                             #tdr.append(apenasDigitos2)
                                             #bb= (apenasDigitos1 - 32) * 5/9
                                             print('chegou aqui 4')
                                             bb= str(int((int(apenasDigitos1) - 32) * 5/9))
                                             print(bb)
                                             tar.append(bb)
                                             bb= str(int((int(apenasDigitos2) - 32) * 5/9))
                                             tdr.append(bb)
                                             print( bb)
                                             
                                            
                                            # print(bb)
                                             #tar.append(bb)
                                             #bb= (apenasDigitos2 - 32) * 5/9
                                             #print(bb)

                                             #tdr.append(bb)

                                            
                                            
    
                                        #elif i==5:
                                           
                                                
                                           # pressao.append(rows[i].contents[j].string)
                                            #print('chegou aqui 5')
                                            #print(rows[i].contents[j].string)

                                        elif i==5:
                                            print('chegou aqui 5555555')
                                            print(rows[i].contents[j].string)
                                            if (rows[i].contents[j].string) !=None:
                                                pressao.append(str(float((rows[i].contents[j].string)) * 33.863)[0:4])
                                            else:
                                                pressao.append(rows[i].contents[j].string) 

                                        
                                        elif i==7:
                                            nbaixa.append(rows[i].contents[j].string)
                                            print('chegou aqui 5')
                                            print(rows[i].contents[j].string)
    
                            except:
                                continue
    
    
                        #estacao='SBGL'*len(tar)
                        estacao=[estacao.upper() for x in range(len(tar))]
                        print(hhh)
                        if hhh=='0<':
                            hhh='00'
                        elif hhh=='1<':
                            hhh='01'
                        elif hhh=='2<':
                            hhh='02'
                        elif hhh=='3<':
                            hhh='03'
                        elif hhh=='4<':
                            hhh='04'
                        elif hhh=='5<':
                            hhh='05'
                        elif hhh=='6<':
                            hhh='06'
                        elif hhh=='7<':
                            hhh='07'
                        elif hhh=='8<':
                            hhh='08'
                        elif hhh=='9<':
                            hhh='09'
                        
                        datahora1=ddd +" "+hhh+":00"
                        print('chegou aqui 7')
                        print(datahora1)
                        
                            
                        
                        print(estacao)
                        print(len(estacao))
                        dia=datahora1[8:10]
                        mes=datahora1[5:7]
                        ano=datahora1[0:4]
                        hor=datahora1[11:16]
                        d = str(dia) + '/' + str(mes) + '/' + str(ano) + ' ' + hor 
                        print(d)
                        print('chegou aqui 8')
                        dateFormatter = "%d/%m/%Y %H:%M"
                        d=datetime.strptime(d, dateFormatter)
                        d=d+timedelta(hours=int(horazulu))
                        print(d)
                        j=0
                        dd=[]
                        datazulu=[]
                        
                        
                        #datetime.strptime(dateString, dateFormatter)
                        for i in range(0,len(estacao),1):
                            try:
                                print(d)
                                dd.append(d)
                                datazulu.append(d)
                                #timestring = datetime.strptime((dada + timedelta(hours=3)), dateFormatter)
                                d=d+timedelta(hours=3)
                                print('chegou aqui 9')
                                #print(timestring)
                               # dd.append(datetime.strptime(d, dateFormatter))
                               # datazulu.append(datetime.strptime(dddd, dateFormatter) + timedelta(hours=int(horazulu)))
                                
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
                        print('chegou aqui 10')
    
                        df= pd.DataFrame(
                            lista_de_tuplas,
                            columns=['estacao','datahora', 'tar', 'tdr', 'pressao','nbaixa','datazulu']
                        )
                        
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
            print(df1)
            return df1
    
    
    def lookup_coord2(city_name,usu):
        """Function to lookup the names of city"""
        print('cheguei aqui -2')
        print(city_name)
        print(usu)
        if usu==1:
            df = pd.read_csv("cities_transformed3.csv")
        else:
            df = pd.read_csv("cities_transformed3.csv")
        print (df)
        city_data = df[df['city'].str.lower() == city_name]
        print(city_data)
        if not city_data.empty:
    
            lat = city_data['lat'].iloc[0]
            lon = city_data['lon'].iloc[0]
            print(lat)
            print(lon)
            return lat, lon
        else:
            return None
    
    
    def sort_data2(weather_data):
        """"Function to extract data from json"""
        def umidade(ta,td):
            if str(ta) =='--' or str(ta) =='//'or str(td) =='//'or str(td)=='--':
                ur='--'
            else:
                a=float(ta)
                b=float(td)
                if a < b:
                    ur='--'
                else:
                    if a >= 0:
                        aa=7.5*a/(237.5+a)
                    else:
                        aa=9.5*a/(265.5+a)
                    u_b=7.5*b
                    c=237.3+b
                    d=((-aa*c)+u_b)/c
                    urr=(10**d)*100
                    if urr>100:
                        urr=100
                    ur=str(int(urr))
            return ur
        
    
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
            #ur= str(round(100 - 5 * (int(temp) - int(td))))
            ur=umidade(temp,td)
            nbaixas=str(weather_data['nbaixa'][i])
            print('NUVENS BAIXAS')
            print(nbaixas)
            if nbaixas[-1]=='k':
                nbaixas=str(int(nbaixas[0:len(nbaixas)-1])*1000)
            elif nbaixas=='--':
                nbaixas = 'Nil'
            else:
                nbaixas=str(int(int((nbaixas))))
            #if len(nbaixas)>5:
            #    nbaixas=nbaixas[0:5]
    
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
            ######extracted_data.append(
             ####   (weather_data['estacao'][i], date, time, temp,
             ######    tp, cld, cldcb,wspd,wdir,gust,visibilidade))
    
        # push_data(extracted_data)
        return extracted_data
    
    
    def authenticate2(city):
    
        """Function to request information from OpenWeatherMap API giving the necessary details"""
        #try:
    
        print('authenticate2------0')
        print(city)
    
        link,data1,horazulu=baixarmodeloNovoprojeto(city)
        print('authenticate2------1')
        ###city='SBJR'
        #####horazulu='3'
        ###link='https://www.windy.com/-22.910/-43.163/meteogram?-22.935,-43.163,13,m:c0YaeXe'
        ##horazulu='3'
        
        data2=baixaamodeloNovometeograma(city,link,horazulu)
        #print(data2)
        print('authenticate2------2')
       
    
        #except Exception as e:
        #    st.error(f"Could not get the data because {e}. Exiting...")
        #    st.stop()
        #data = pd.read_csv("dadosecmwf_area2_1104.csv")
        print('authenticate2')
        data=pd.merge(data1, data2, how='inner', on='datahora')
        
        data1=data.drop(['tar_y', 'estacao_y', 'datazulu_y'], axis=1)
        
        
        data4=data1.rename(columns={'estacao_x': 'estacao', 'tar_x': 'tar', 'datazulu_x': 'datazulu'})
        
    
    
        return data4
    
    def search2(city,usu):
        from time import sleep
        try:
            print('cheguei -1')
            
            lat, lon = lookup_coord2(city,usu)
                # st.write(lat)
            print('cheguei 0')

            for x in range(0, 4):  # try 4 times
                try:
                    data = authenticate2(city)
                except Exception as str_error:
                    print('cheguei aqui search222')
                    pass
                else:
                    break
                
            
            
                # st.write(data)
            print('cheguei aqui search2')
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
        from datetime import datetime
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
            # min_max_df = pd.DataFrame({'max_temp': df.groupby('date')['max_temp'].max(), 'date': df['date'].unique(), 'min_temp':df.groupby('date')['min_temp'].min()})
            # fig = px.line(min_max_df, x= 'date', y=['max_temp','min_temp'],title='Minimum and Maximum Temperature')
            # new = {'max_temp':'Maximum Temperature', 'min_temp': 'Minimum Temperature'}
            # fig.for_each_trace(lambda t: t.update(name = new[t.name]))
        ####df['data'].unique()[0:len(df['data'].unique()) - 1]
        #####df.groupby('data')['temp'].max()[0:len(df['data'].unique()) - 1]
       # auxy=df.groupby('data')['temp'].max()[0:len(df['timestamp'].unique()) - 1]
        #auxy=auxy.sort_index(ascending=True)
        #df['data']=pd.to_datetime(df['data'])
        df['data']=df.data.apply(lambda linha: datetime.strptime(linha, "%d/%m/%Y"))
        auxy=df.groupby('data')['temp'].max()[0:len(df['data'].unique()) - 1]
        fig = go.Figure()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        x=df['data'].unique()[0:len(df['data'].unique()) - 1]
        y1=df.groupby('data')['temp'].max()[0:len(df['data'].unique()) - 1]
        y2 =df.groupby('data')['temp'].min()[0:len(df['data'].unique()) - 1]
    
        fig.add_trace(go.Scatter(x=x, y=y1,
                                 mode='lines',
                                 marker_color='red',
                                 name='Temperatura Máxima'), secondary_y=False)
        fig.add_trace(go.Scatter(x=x, y=y2,
                                 mode='lines',
                                 marker_color='blue',
                                 name='Temperatura Mínima'), secondary_y=False)
        fig.update_yaxes(title="Temperatura (°C)")
        fig.update_xaxes(title="dia")
        fig.update_layout(title_text="Temperaturas Máxima e Mínima")
    
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
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
       ## """Container for minimum and maximum temperatures"""
        # min_max_df = pd.DataFrame({'max_temp': df.groupby('date')['max_temp'].max(), 'date': df['date'].unique(), 'min_temp':df.groupby('date')['min_temp'].min()})
        # fig = px.line(min_max_df, x= 'date', y=['max_temp','min_temp'],title='Minimum and Maximum Temperature')
        # new = {'max_temp':'Maximum Temperature', 'min_temp': 'Minimum Temperature'}
        # fig.for_each_trace(lambda t: t.update(name = new[t.name]))

        fig = go.Figure()
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        x =x=df['data'].unique()
        y1 = df.groupby('data')['temp_max'].max()
        y2 = df.groupby('data')['temp_min'].min()

        fig.add_trace(go.Scatter(x=x, y=y1,
                                 mode='lines',
                                 marker_color='red',
                                 name='Temperatura Máxima'), secondary_y=False)
        fig.add_trace(go.Scatter(x=x, y=y2,
                                 mode='lines',
                                 marker_color='blue',
                                 name='Temperatura Mínima'), secondary_y=False)
        fig.update_yaxes(title="Temperatura (°C)")
        fig.update_xaxes(title="dia")
        fig.update_layout(title_text="Temperaturas Máxima e Mínima")





        # fig = px.scatter(title='Temperatura máxima e mínima')
        # fig.add_scatter(x=df['data'].unique(), y=df.groupby('data')['temp_max'].max(), name='Temperatura Máxima')
        # fig.add_scatter(x=df['data'].unique(), y=df.groupby('data')['temp_min'].min(), name='Temperatura Mínima')
        # fig.update_yaxes(title="Temperatura (°C)")
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
                            'SBAC','SBJE', 'SBPB', 'SNRU','SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU',
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
                    df1=df
                    df1.drop('sea_level', inplace=True, axis=1)
                    df1.drop('grnd_level', inplace=True, axis=1)
                    df1.drop('temp_min', inplace=True, axis=1)
                    df1.drop('temp_max', inplace=True, axis=1)

                   
                    
                    st.table(df1)
    elif modelo=="ECMWF":


        #usuario = st.radio("Escolha o usuário", ["Previsor(CMA-GL)", "Público Geral"], disabled=True,on_change='hidden')
        
        #button='SBRJ'
       # city='SBRJ'
        if button or city:
            if not city:
                pass
                
            
            
            result, lat, lon = search2(city, usu)
            
                
            
            # st.write(result)
            df = pd.DataFrame(result)
            df1 = pd.DataFrame(result)
           
            df.rename(
                columns={0: 'estacao', 1: 'data', 2: 'hora', 3: 'temp', 4: 'ur', 5: 'pressao', 6: 'tp',
                         7: 'ceu',8: 'ncb',9: 'int vento',
                         10: 'dir vento', 11: 'raj vento', 12: 'visibilidade', 13: 'nbaixas'}, inplace=True)
            ##df.rename(
             ##   columns={0: 'estacao', 1: 'data', 2: 'hora', 3: 'temp', 4: 'tp',
              ##           5: 'ceu',6: 'ncb',7: 'int vento',
               ##          8: 'dir vento', 9: 'raj vento', 10: 'visibilidade'}, inplace=True)



            
            df['timestamp'] = (df['data'] + ' ' + df['hora'])
           
            print('final')
            print(df)
           
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
                from datetime import tzinfo, timedelta, datetime
                stp = ""
                horz= datetime.utcnow()

                ll=0
                while horz.strftime("%d/%m/%Y %H:00")>df['timestamp'][ll]:
                    ll=ll+1
                    horz=horz + timedelta(hours=1)

                datcomp=horz.strftime("%d/%m/%Y %H:00")




                st.header(f"{city.capitalize().upper()}, BR {emoji(df['tp'].iloc[ll])}")
                st.subheader(str(df['timestamp'].iloc[ll])[0:16] + 'UTC')
                col1, col2, col3 = st.columns(3)
                with col1:
                    col1.metric("Temperatura(°C)", f"{(df['temp'].iloc[ll])}")
                    if df['ceu'].iloc[ll] == 'FEW':
                        sceu = 'Poucas nuvens'
                    elif df['ceu'].iloc[ll] == 'SCT':
                        sceu = 'Parcialmente nublado'
                    elif df['ceu'].iloc[ll] == 'BKN':
                        sceu = 'Nublado'
                    elif df['ceu'].iloc[ll] == 'OVC':
                        sceu = 'Encoberto'
                    else:
                        sceu = 'Claro'

                    # col1.metric("Céu", f"{df['ceu'].iloc[0]}")
                    col1.metric("Céu", sceu)
                    col1.metric("Umidade(%)", f"{df['ur'].iloc[ll]}")

                with col2:
                    if df['tp'].iloc[ll] == 'BR':
                        stp = 'Névoa'
                    elif df['tp'].iloc[ll] == 'RA':
                        stp = 'Chuva'
                    elif df['tp'].iloc[ll] == 'TS':
                        stp = 'Trovoada'
                    elif df['tp'].iloc[ll] == 'TSRA':
                        stp = 'Trovoada com chuva'
                    else:
                        stp = 'Nil'
                    # col2.metric("Tempo presente", f"{(df['tp'].iloc[0])}")
                    col2.metric("Tempo presente", stp)
                    col2.metric("Visibilidade(m)", f"{df['visibilidade'].iloc[ll]}")
                    col2.metric("Pressão(hPa)", f"{df['pressao'].iloc[ll]}")
                with col3:
                    # col3.metric("Tempo", f"{df['tp'].iloc[0]}")
                    col3.metric("Rajada(kt)", f"{(df['raj vento'].iloc[ll])}")
                    col3.metric("Vento(graus/kt)", f"{(df['dir vento'].iloc[ll])} / {int(df['int vento'].iloc[ll])}")
                    col3.metric("Altura nuvens baixas(ft)", f"{df['nbaixas'].iloc[ll]}")

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
                    df1=df
                    df1.drop('data', inplace=True, axis=1)
                    df1.drop('hora', inplace=True, axis=1)
                    		#pressao	tp	ceu	ncb	int vento	dir vento	raj vento	visibilidade	nbaixas
                    df1 = df1.reindex(['estacao','timestamp', 'temp', 'ur','pressao', 'tp','ceu','ncb','int vento','dir vento','raj vento','visibilidade','nbaixas'], axis=1)
                    #df1['data']=(str(df['timestamp'].iloc)[0:10])
                    st.table(df1)

main()



