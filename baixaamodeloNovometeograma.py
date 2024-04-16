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

#arqi=pd.read_csv('estacaomodeloicon.csv', encoding='iso-8859-1', delimiter =';')





#link='https://www.windy.com/-22.910/-43.163/meteogram?-22.935,-43.163,13,m:c0YaeXe' #meteograma
def Scraper(estacao,link,horazulu):
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
                    print('chegou aqui bm222')
                    print(link1)
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
