import time  # to simulate a real time data, time loop

#import redemet
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
from bokeh.plotting import figure
#from PyInstaller.utils.hooks import collect_data_files
import os.path
# from datetime import date
# from datetime import datetime
from datetime import datetime, timedelta, date
from os import makedirs as mkdir

import emoji
#import metpy.calc as mpcalc
# import numpy as np
import pandas as pd
# from bokeh.io import output_file, show
# from bokeh.io import output_file, show
# from bokeh.layouts import gridplot
# from bokeh.plotting import figure
from bokeh.plotting import figure, output_file, show, save
from bokeh.plotting import save
# from bokeh.sampledata.periodic_table import elements
from bokeh.sampledata.periodic_table import elements
# from bokeh.transform import dodge, factor_cmap
from bokeh.transform import dodge, factor_cmap
#from metpy.units import units
from PIL import Image
global diaini, mesini
from bokeh.resources import CDN
from bokeh.embed import file_html



def umidade(ta,td):
        if str(ta) =='--' or str(ta) =='//'or str(td) =='//'or str(td)=='--' or int(td) > int(ta):
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
def obterarq(estacaop,areap,datainicial):
        import plotly.graph_objects as go
        #import metpy.calc as mpcalc
        #from metpy.units import units

        import numpy as np
        #from datetime import datetime
        #from datetime import date
        import pandas as pd
        import re
        import plotly

        import plotly.express as px

        # %% histogram with wind directions
        #date_inicio = datetime.strptime(datainicial, '%d/%m/%y')
        datainicial=datainicial + timedelta(0)
        pd.set_option('max_columns', None)
        pd.set_option('max_columns', None)
        # arqi1=pd.read_csv('metar_trat_area2_tabuleiro_rosa.csv')
        if areap==1:
            arqi1 = pd.read_csv('metar_trat_teste1.csv')
        else:
            arqi1 = pd.read_csv('metar_trat_teste2.csv')

        arqi = arqi1.loc[(arqi1['estacao'] == estacaop)]
        #arqi = arqi.reset_index(drop=True)
        x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in arqi.datahora]
        arqi['data_hora'] = x
        ddata = arqi.data_hora
        diai = arqi['data_hora']
        ur=[]
        arqi['drytt'] = arqi['dryt']
        arqi['drytt'].fillna(0, inplace=True)
        arqi['dewpt'] = arqi['dewp']
        arqi['dewpt'].fillna(0, inplace=True)
        arqi.sort_values(by=['data_hora'], inplace=True)
        arqi = arqi.reset_index(drop=True)
        arqi = arqi.loc[(arqi['data_hora'] >= datainicial.strftime('%Y-%m-%d'))]
        print('chegou aqui')
        print(datainicial.strftime('%d/%m/%Y %H:%M'))
        arqi.sort_values(by=['data_hora'], inplace=True)
        arqi = arqi.reset_index(drop=True)

        for pp in range(0,len(arqi),1):


            #ur.append (round(mpcalc.relative_humidity_from_dewpoint(float((arqi.drytt[pp])) * units.degC, float((arqi.dewpt[pp])) * units.degC).magnitude * 100), 0)
            #ur.append(round(100 - 5 * (float(arqi['dryt'][pp]) - float(arqi['dewp'][pp]))))
            #print(arqi['drytt'][pp])
            #print(arqi['dewpt'][pp])
            umid=umidade(arqi['drytt'][pp],arqi['dewpt'][pp])
            if umid=='--':
                ur.append(-99)
            else:
                ur.append(int(umid))
        arqi['ur']=ur
        arqi.sort_values(by=['data_hora'], inplace=True)
        arqi = arqi.reset_index(drop=True)






        return arqi

def weather_pie(df):
        ###"""Container for pie chart of weather conditions"""
        df['tp'].replace({'<NA>': float('nan'), pd.NA: 'Nil'}, inplace=True)
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
            # auxy=auxy.sort_index(ascending=True)
            # df['data']=pd.to_datetime(df['data'])
            df['data1'] = df['datahora'].str.slice(0, 10)
            df['data'] = df.data1.apply(lambda linha: datetime.strptime(linha, "%d/%m/%Y"))
            auxy = df.groupby('data')['dryt'].max()[0:len(df['data'].unique()) - 1]
            fig = go.Figure()
            #fig = make_subplots(specs=[[{"secondary_y": True}]], subplot_titles='Temperaturas Máxima e Mìnima')
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            x = df['data'].unique()[0:len(df['data'].unique()) - 1]
            y1 = df.groupby('data')['dryt'].max()[0:len(df['data'].unique()) - 1]
            y2 = df.groupby('data')['dryt'].min()[0:len(df['data'].unique()) - 1]
    
            fig.add_trace(go.Scatter(x=x, y=y1,
                                     mode='lines',
                                     marker_color='red',
                                     name='Temperatura Máxima'), secondary_y=False)
            fig.add_trace(go.Scatter(x=x, y=y2,
                                     mode='lines',
                                     marker_color='blue',
                                     name='Temperatura Mínima'), secondary_y=False)
            fig.update_yaxes(title="Temperatura (°C)")
            fig.update_xaxes(title="Data")
            fig.update_layout(title_text="Temperaturas Máxima e Mínima")
    
            st.plotly_chart(fig, use_container_width=True)
            return

def vento2(df):
        ##"""Container for temperature time series"""
        # vento_df = pd.DataFrame(
        #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})

        fig = px.scatter(title='Vento')
        fig.add_scatter(x=df['data_hora'], y=df['wspd'], name='Int.vento(kt)')
        fig.add_scatter(x=df['data_hora'], y=df['wdir'], name='Dir.vento(graus)')
        fig.update_yaxes(title="Valor")
        fig.update_xaxes(title="Data")
        st.plotly_chart(fig, use_container_width=True)
        return

def temp_time_series2(df):
        ###"""Container for temperature time series"""
        temp_time_df = pd.DataFrame(
            {'temp': df['dryt'], 'ur': df['ur'], 'timestamp': df['data_hora']})
        fig = px.line(temp_time_df, x='timestamp', y=['temp', 'ur'],
                      title='Temperatura(°C) e Umidade Relativa(%)')
        fig.update_yaxes(title="Valor")
        fig.update_xaxes(title="Data")
        new = {'temp': 'Temperatura Atual(°C)', 'ur': 'Umidade (%)'}
        fig.for_each_trace(lambda t: t.update(name=new[t.name]))
        # fig.update_legends(selector={'actual_temp': 'Air Temperature'})
        # fig = px.scatter(title='Temp')
        # fig.add_scatter(x=df['timestamp'], y=df['actual_temp'],mode='lines',name='Actual Temperature')
        # fig.add_scatter(x=df['timestamp'], y=df['feels_like_temp'],mode='lines',name='Feels-like Temperature')
        # fig.update_xaxes(title="Date", tickformat="%d-%m-%Y")
        # fig.update_yaxes(title="Temperature (°C)", range=[df['min_temp'].min(), df['max_temp'].max()])
        st.plotly_chart(fig, use_container_width=True)
    
def rest(areas,to_data,from_data,tipo):
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
                #global df,arqi
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
                return df
    
            df=criadataframe()
            estado=areasele
            areatrab=areasele
    
            arqi = pd.read_csv('metar111.csv',
                               sep=',',
                               # index_col=0,
                               parse_dates=True,
                               dayfirst=True,
                               decimal='.',on_bad_lines='skip')
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

                if len(str(arqi.Mensagem[i])) ==3:
                      ggggg=1
                      mensagem1='NAN'

                elif arqi.Mensagem[i].find('COR') > -1:
                    novamens = 'METAR ' + arqi.Mensagem[i][arqi.Mensagem[i].find('COR') + 4:len(arqi.Mensagem[i])]

                    mensagem1 = novamens.split()
                    mens = novamens

                else:

                    mensagem1 = arqi.Mensagem[i].split()
                    mens = arqi.Mensagem[i]

    
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
                        if mensagem1[j].find('SB') > -1 or mensagem1[j].find('SSKW') > -1 or mensagem1[j].find('SWPI') > -1 or mensagem1[j].find('SWEI') > -1 or mensagem1[j].find('SNRU') > -1:
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
                            if (mensagem1[j][3:5]) == '//' or (mensagem1[j][3:5]) == '/ ' or (mensagem1[j][3:5]) == '/' or  mensagem1[j].find('///') > -1:
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
            print('ESTADO: ',estado)
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

           
def redemet_baixa2(escolha, ar, datahini, datahfim, estacao1):
            
            import datetime
            import time
            import requests
            import pandas as pd
            import json
            from datetime import datetime, timedelta, date
            from pandas.io.json import json_normalize
            from bs4 import BeautifulSoup
            dtini = '20240426'
            #estacao1=estacao1[0:len(estacao1)-1]
            f = open("metar111.csv", "w")
            if (datahfim - datahini).days==0:
                intervalo=0
            else:
                intervalo=(datahfim - datahini).days
            print('cheguei aqui 3')
            print(intervalo)
            cab = ',Localidade,Tipo,Data,Mensagem'
            arquivo = []
            f.write(cab)
            arquivo.append(cab)

            for j in range(0,intervalo+1,1):
                datahinic=datahini + timedelta(days=j)
                ano = str(datahinic)[0:4]
                mes = str(datahinic)[5:7]
                dia = str(datahinic)[8:10]
                datainicio = dia + '/' + mes + '/' + ano

                 # url = 'https://redemet.decea.gov.br//api/consulta_automatica/index.php?local=sbbr,sbgl,sbsp&msg=metar&data_ini=2023041900&data_fim=2023041923&saida_html=SIM'
                url = 'https://redemet.decea.gov.br//api/consulta_automatica/index.php?local='+estacao1+'&msg=metar&data_ini=' + ano+mes+dia + '00&data_fim=' + ano+mes+dia + '23&saida_html=SIM'
                print('cheguei 1')
                print(url)
                res = requests.get(url)
                soup = BeautifulSoup(res.content, "lxml")
                s = soup.select('html')[0].text.strip('jQuery1720724027235122559_1542743885014(').strip(')')
                s = s.replace('null', '"placeholder"')
                s = s.replace('- ', ',')
                p = s.split(',')
                print('cheguei 2')
                print(p)
               
                for i in range(1, len(p), 1):
                    if p[i].find('METAR') > -1:
                        b = 'METAR'
                    else:
                        b = 'SPECI'
                    if p[i].find('SB') > -1:
                        a = p[i][p[i].find('SB'):p[i].find('SB') + 4]  # or p[i].find('SSKW') > -1 or mensagem1[i].find('SWPI') > -1 or mensagem1[i].find('SWEI') > -1:
                    elif p[i].find('SSKW') > -1:
                        a = 'SSKW'
                    elif p[i].find('SWPI') > -1:
                        a = 'SWPI'
                    elif p[i].find('SWEI') > -1:
                        a = 'SWEI'
                    elif p[i].find('SNRU') > -1:
                        a = 'SNRU'

                    montalinha = str(i) + ',' + a + ',' + b + ',' + datainicio + ',' + p[i][0:p[i].find('=') + 1]
                    arquivo.append(montalinha)
                    f.write("\n" + montalinha)
            #f.close
            return arquivo
    
        
def baixa_aws(ar):
            import urllib.request
            import re
            from bs4 import BeautifulSoup
            import requests
            import pandas as pd
        
            from datetime import datetime, timedelta
            # importe as funções BeautifulSoup para analisar os dados retornados do site
            from bs4 import BeautifulSoup
        
            # especifique o URL
            if ar == 1:
                url="https://aviationweather.gov/api/data/metar?ids=SBJR%2CSBAC%2CSBAR%2CSBCB%2CSBCP%2CSBES%2CSBFS%2CSBFN%2CSBFZ%2CSBGL%2CSBJE%2CSBJP%2CSBJU%2CSBKG%2CSBME%2CSBMO%2CSBMS%2CSBNT%2CSBPB%2CSBPJ%2CSBPL%2CSBPS%2CSBRF%2CSBRJ%2CSBSL%2CSBSG%2CSBTE%2CSBVT%2CSNRU&format=html&hours=96"
        
            else:
                # wiki = "https://www.aviationweather.gov/metar/data?ids=SBRD%2CSBVH%2CSBJI%2CSBRB%2CSSKW%2CSBCY%2CSBPV%2CSBCZ%2CSBTT%2CSBIZ%2CSBCI%2CSBMA%2CSBCJ%2CSBHT%2CSBTB%2CSBOI%2CSWPI%2CSBBE%2CSBMQ%2CSBSN%2CSBSO%2CSBSI%2CSBAT%2CSBIH%2CSBMY%2CSBTF%2CSBUA%2CSBEG%2CSBBV&format=raw&date=&hours=24"
                url='https://aviationweather.gov/api/data/metar?ids=SBRD%2CSBVH%2CSWEI%2CSBUY%2CSBJI%2CSBRB%2CSSKW%2CSBCY%2CSBPV%2CSBCZ%2CSBTT%2CSBIZ%2CSBCI%2CSBMA%2CSBCJ%2CSBHT%2CSBTB%2CSBOI%2CSWPI%2CSBBE%2CSBMQ%2CSBSN%2CSBSO%2CSBSI%2CSBAT%2CSBIH%2CSBMY%2CSBTF%2CSBUA%2CSBEG%2CSBBV&format=html&hours=96'
            # Consulte o site e retorne o html para a variável 'page'
        
            res = requests.get(url)
            soup = BeautifulSoup(res.content, "lxml")
        
            # Parse o html na variável 'page' e armazene-o no formato BeautifulSoup
            p = soup.select('html')[0].text.strip('jQuery1720724027235122559_1542743885014(').strip(')').split('\n\n\n')
            metar = []
            data = []
        
            metari = []
            dataaux = datetime.utcnow()
            dataaux = datetime.utcnow() - timedelta(hours=96)
            mesnow = datetime.utcnow().month
            mesant = (datetime.utcnow() - timedelta(hours=96)).month
            # diaini = list_item[0].contents[0].split()[1][0:2]
            controledia = False
            controlemens = False
            for i in range(0, len(p), 1):
                if p[i].find('METAR') > -1:
                    b = 'METAR'
                    controlemens = True
                elif p[i].find('SPECI') > -1:
                    b = 'SPECI'
                    controlemens = True
                if p[i].find('UTC') > -1:
                    # diaini=p[i] [p[i].find('UTC') -5 :p[i].find('UTC') -3]
                    diaini = p[i][p[i].find('UTC') + 4:p[i].find('UTC') + 6]
                    controledia = True
        
                if p[i].find('Text:') > -1:
                    inicio = p[i].find('Text:')
                    a = p[i][p[i].find('SB'):p[i].find(
                        'SB') + 4]  # or p[i].find('SSKW') > -1 or mensagem1[i].find('SWPI') > -1 or mensagem1[i].find('SWEI') > -1:
                elif p[i].find('SSKW') > -1:
                    a = 'SSKW'
                elif p[i].find('SWPI') > -1:
                    a = 'SWPI'
                elif p[i].find('SWEI') > -1:
                    a = 'SWEI'
                elif p[i].find('SNRU') > -1:
                    a = 'SNRU'
                if controlemens == True:
                    montalinha = p[i][p[i].find('Text:') + 5: len(p[i])] + '='
                    controlemens = False
                if controledia == True:
                    mes = mesnow
                    ano = datetime.utcnow().year
                    dataini = str(diaini) + '/' + str(mes) + '/' + str(ano)
                    metar.append([dataini, 'METAR ' + montalinha])
        
                    controledia = False
                # montalinha = str(i) + ',' + a + ',' + b + ',' + datainicio + ',' + p[i][0:p[i].find('=') + 1]
                # diaini = list_item[0].contents[0].split()[1][0:2]
        
            p = 1
            data_df = pd.DataFrame(metar, columns=['Data', 'Mensagem'])
            file = data_df.to_csv("metar111.csv")
        
            
                        # df = df.drop(columns=['Unnamed: 0'])
            #os.chdir("/mount/src/edomenico/area1")
            #df.to_csv("metar111.csv",encoding='utf-8', index=False,date_format='%d/%m/%Y %H:%M')
            # df.to_csv('example.csv')
            return file
start_date = datetime.today()
end_date = datetime.today()
        
area = ['Área 1', 'Área 2']
area_1 = ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
                  'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SNRU','SBFN', 'SBPL',
                  'SBPJ']
area_2 = ['SBRD', 'SBVH', 'SBJI', 'SSKW','SBRB','SWEI','SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA', 'SBCJ', 'SBHT',
                  'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SWPI', 'SBMY', 'SBTF', 'SBUA', 'SBEG',
                  'SBBV']
        # st.set_page_config(
        #         page_title="Dados Estatísticos",
        #         page_icon="✅",
        #         layout="wide",
        #     )
       # barra_lateral = st.sidebar.empty()
        #area_seleciona = st.sidebar.selectbox("Seleciona a área:", area)
       # if area_seleciona == 'Área 1':
       #     areaprev=1
       #     areasel = area_1
       #     estacao = 'SBJR,SBAC,SBAR,SBCB,SBCP,SBES,SBFS,SBFN,SBFZ,SBGL,SBJE,SBJP,SBJU,SBKG,SBME,SBMO,SBMS,SBNT,SBPB,SNRU,SBPJ,SBPL,SBPS,SBRF,SBRJ,SBSL,SBSG,SBTE,SBVT,'
       # else:
        ##    areasel = area_2
        #    estacao = 'SBRD,SBVH,SWEI,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SWPI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SBTF,SBUA,SBEG,SBBV,'
        #to_data = st.sidebar.date_input('Inicio:', start_date)
        #from_data = st.sidebar.date_input('Fim:', end_date)
        #datainicio = datetime.utcnow()
       # to_data = datainicio.strftime("%d/%m/%Y")
       # from_data = to_data
    
if areas==1:
            areasel=area_1
            areaprev = 1
            estacao = 'SBJR,SBAC,SBAR,SBCB,SBCP,SBES,SBFS,SBFN,SBFZ,SBGL,SBJE,SBJP,SBJU,SBKG,SBME,SBMO,SBMS,SBNT,SBPB,SNRU,SBPJ,SBPL,SBPS,SBRF,SBRJ,SBSL,SBSG,SBTE,SBVT,'
else:
            areasel=area_2
            areaprev = 2
            estacao = 'SBRD,SBVH,SWEI,SBUY,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SWPI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SBTF,SBUA,SBEG,SBBV,'
if tipo=='REDEMET':
            print('area sel - redemet',areasel)
            pdf= redemet_baixa2(1, areasel, to_data, from_data,estacao)
else:
            print('area sel',areasel)
            pdf= baixa_aws(areaprev)
        
pdff=trata_redemet(areaprev)
        #edited_df = st.data_editor(pdff)
def _data_url_to_image(data_url: str) -> Image:
            """Convert DataURL string to the image."""
            _, _data_url = data_url.split(";base64,")
            return Image.open(io.BytesIO(base64.b64decode(_data_url)))

def tabuleiro(est,areatrab,datainicio):
        print('DATAINICIO')
        print(datainicio)
        
        def formata():
            from bokeh.models import FuncTickFormatter, FixedTicker
            p.xaxis.ticker = FixedTicker(ticks=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

            if diaini == 1:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 1, 2: 2, 3: 3, 4: 4, 5:5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10};
                    return mapping[tick];
                """)
            if diaini == 2:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 2, 2: 3, 3: 4, 4: 5, 5:6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11};
                    return mapping[tick];
                """)

            if diaini == 3:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 3, 2: 4, 3: 5, 4: 6, 5:7, 6: 8, 7: 9, 8: 10, 9: 11, 10: 12};
                    return mapping[tick];
                """)

            if diaini == 4:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 4, 2: 5, 3: 6, 4: 7, 5:8, 6: 9, 7: 10, 8: 11, 9: 12, 10: 13};
                    return mapping[tick];
                """)

            if diaini == 5:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 5, 2: 6, 3: 7, 4: 8, 5:9, 6: 10, 7: 11, 8: 12, 9: 13, 10: 14};
                    return mapping[tick];
                """)

            if diaini == 6:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 6, 2: 7, 3: 8, 4: 9, 5:10, 6: 11, 7: 12, 8: 13, 9: 14, 10: 15};
                    return mapping[tick];
                """)

            if diaini == 7:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 7, 2: 8, 3: 9, 4: 10, 5:11, 6: 12, 7: 13, 8: 14, 9: 15, 10: 16};
                    return mapping[tick];
                """)
            if diaini == 8:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 8, 2: 9, 3: 10, 4: 11, 5:12, 6: 13, 7: 14, 8: 15, 9: 16, 10: 17};
                    return mapping[tick];
                """)
            if diaini == 9:
                p.xaxis.formatter = FuncTickFormatter(code="""
                    var mapping = {1: 9, 2: 10, 3: 11, 4: 12, 5:13, 6: 14, 7: 15, 8: 16, 9: 17, 10: 18};
                    return mapping[tick];
                """)
            if diaini == 10:
                p.xaxis.formatter = FuncTickFormatter(code="""
                       var mapping = {1: 10, 2: 11, 3: 12, 4: 13, 5:14, 6: 15, 7: 16, 8: 17, 9: 18, 10: 19};
                       return mapping[tick];
                   """)
            if diaini == 11:
                p.xaxis.formatter = FuncTickFormatter(code="""
                       var mapping = {1: 11, 2: 12, 3: 13, 4: 14, 5:15, 6: 16, 7: 17, 8: 18, 9: 19, 10: 20};
                       return mapping[tick];
                   """)
            if diaini == 12:
                p.xaxis.formatter = FuncTickFormatter(code="""
                          var mapping = {1: 12, 2: 13, 3: 14, 4: 15, 5:16, 6: 17, 7: 18, 8: 19, 9: 20, 10: 21};
                          return mapping[tick];
                      """)
            if diaini == 13:
                p.xaxis.formatter = FuncTickFormatter(code="""
                          var mapping = {1: 13, 2: 14, 3: 15, 4: 16, 5:17, 6: 18, 7: 19, 8: 20, 9: 21, 10: 22};
                          return mapping[tick];
                      """)
            if diaini == 14:
                p.xaxis.formatter = FuncTickFormatter(code="""
                          var mapping = {1: 14, 2: 15, 3: 16, 4: 17, 5:18, 6: 19, 7: 20, 8: 21, 9: 22, 10: 23};
                          return mapping[tick];
                      """)
            if diaini == 15:
                p.xaxis.formatter = FuncTickFormatter(code="""
                            var mapping = {1: 15, 2: 16, 3: 17, 4: 18, 5:19, 6: 20, 7: 21, 8: 22, 9: 23, 10: 24};
                            return mapping[tick];
                      """)
            if diaini == 16:
                p.xaxis.formatter = FuncTickFormatter(code="""
                            var mapping = {1: 16, 2: 17, 3: 18, 4: 19, 5:20, 6: 21, 7: 22, 8: 23, 9: 24, 10: 25};
                            return mapping[tick];
                       """)
            if diaini == 17:
                p.xaxis.formatter = FuncTickFormatter(code="""
                            var mapping = {1: 17, 2: 18, 3: 19, 4: 20, 5:21, 6: 22, 7: 23, 8: 24, 9: 25, 10: 26};
                            return mapping[tick];
                       """)
            if diaini == 18:
                p.xaxis.formatter = FuncTickFormatter(code="""
                            var mapping = {1: 18, 2: 19, 3: 20, 4: 21, 5:22, 6: 23, 7: 24, 8: 25, 9: 26, 10: 27};
                            return mapping[tick];
                       """)
            if diaini == 19:
                p.xaxis.formatter = FuncTickFormatter(code="""
                            var mapping = {1: 19, 2: 20, 3: 21, 4: 22, 5:23, 6: 24, 7: 25, 8: 26, 9: 27, 10: 28};
                            return mapping[tick];
                       """)
            if diaini == 20:

                if mesini == 2:
                    if (date.today().year % 4) !=0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                            var mapping = {1: 20, 2: 21, 3: 22, 4: 23, 5:24, 6: 25, 7: 26, 8: 27, 9: 28, 10: 1};
                                            return mapping[tick];
                                       """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                    var mapping = {1: 20, 2: 21, 3: 22, 4: 23, 5:24, 6: 25, 7: 26, 8: 27, 9: 28, 10: 29};
                                                                    return mapping[tick];
                                                               """)

                else:

                    p.xaxis.formatter = FuncTickFormatter(code="""
                                var mapping = {1: 20, 2: 21, 3: 22, 4: 23, 5:24, 6: 25, 7: 26, 8: 27, 9: 28, 10: 29};
                                return mapping[tick];
                           """)
            if diaini == 21:
                print('DIA INICIO')
                print(diaini)
                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                            var mapping = {1: 21, 2: 22, 3: 23, 4: 24, 5:25, 6: 26, 7: 27, 8: 28, 9: 1, 10: 2};
                                            return mapping[tick];
                                       """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                    var mapping = {1: 21, 2: 22, 3: 23, 4: 24, 5:25, 6: 26, 7: 27, 8: 28, 9: 29, 10: 1};
                                                                    return mapping[tick];
                                                               """)

                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                var mapping = {1: 21, 2: 22, 3: 23, 4: 24, 5:25, 6: 26, 7: 27, 8: 28, 9: 29, 10: 30};
                                return mapping[tick];
                           """)
            if diaini == 22:

                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                            var mapping = {1: 22, 2: 23, 3: 24, 4: 25, 5:26, 6: 27, 7: 28, 8: 1, 9: 2, 10: 3};
                                            return mapping[tick];
                                       """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                    var mapping = {1: 22, 2: 23, 3: 24, 4: 25, 5:26, 6: 27, 7: 28, 8: 29, 9: 1, 10: 2};
                                                                    return mapping[tick];
                                                               """)

                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                           var mapping = {1: 22, 2: 23, 3: 24, 4: 25, 5:26, 6: 27, 7: 28, 8: 29, 9: 30, 10: 31};
                                           return mapping[tick];
                                       """)
                else:

                    p.xaxis.formatter = FuncTickFormatter(code="""
                               var mapping = {1: 22, 2: 23, 3: 24, 4: 25, 5:26, 6: 27, 7: 28, 8: 29, 9: 30, 10: 1};
                               return mapping[tick];
                           """)
            if diaini == 23:
                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                            var mapping = {1: 23, 2: 24, 3: 25, 4: 26, 5:27, 6: 28, 7: 1, 8: 2, 9: 3, 10: 4};
                                            return mapping[tick];
                                       """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                    var mapping = {1: 23, 2: 24, 3: 25, 4: 26, 5:27, 6: 28, 7: 29, 8: 1, 9: 2, 10: 3};
                                                                    return mapping[tick];
                                                               """)
                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                           var mapping = {1: 23, 2: 24, 3: 25, 4: 26, 5:27, 6: 28, 7: 29, 8: 30, 9: 31, 10: 1};
                                           return mapping[tick];
                                       """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                                       var mapping = {1: 23, 2: 24, 3: 25, 4: 26, 5:27, 6: 28, 7: 29, 8: 30, 9: 1, 10: 2};
                                                       return mapping[tick];
                                                   """)

            if diaini == 24:
                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 24, 2: 25, 3: 26, 4: 27, 5:28, 6: 1, 7: 2, 8: 3, 9: 4, 10: 5};
                                               return mapping[tick];
                                          """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                   var mapping = {1: 24, 2: 25, 3: 26, 4: 27, 5:28, 6: 29, 7: 1, 8: 2, 9: 3, 10: 4};
                                                                   return mapping[tick];
                                                              """)

                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 24, 2: 25, 3: 26, 4: 27, 5:28, 6: 29, 7: 30, 8: 31, 9:1, 10:2};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                              var mapping = {1: 24, 2: 25, 3: 26, 4: 27, 5:28, 6: 29, 7: 30, 8: 1, 9:2, 10:3};
                                              return mapping[tick];
                                         """)

            if diaini == 25:
                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 25, 2: 26, 3: 27, 4: 28, 5:1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6};
                                               return mapping[tick];
                                          """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                   var mapping = {1: 25, 2: 26, 3: 27, 4: 28, 5:29, 6: 1, 7: 2, 8: 3, 9: 4, 10: 5};
                                                                   return mapping[tick];
                                                              """)
                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 25, 2: 26, 3: 27, 4: 28, 5:29, 6: 30, 7: 31, 8: 1, 9: 2, 10: 3};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 25, 2: 26, 3: 27, 4: 28, 5:29, 6: 30, 7: 1, 8: 2, 9: 3, 10: 4};
                                               return mapping[tick];
                                          """)

            if diaini == 26:
                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                   var mapping = {1: 26, 2: 27, 3: 28, 4: 1, 5:2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7};
                                                   return mapping[tick];
                                              """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                           var mapping = {1: 26, 2: 27, 3: 28, 4: 29, 5:1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6};
                                                                           return mapping[tick];
                                                                      """)

                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:

                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 26, 2: 27, 3: 28, 4: 29, 5:30, 6: 31, 7: 1, 8: 2, 9: 3, 10: 4};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 26, 2: 27, 3: 28, 4: 29, 5:30, 6: 1, 7: 2, 8: 3, 9: 4, 10: 5};
                                               return mapping[tick];
                                          """)

            if diaini == 27:
                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 27, 2: 28, 3: 1, 4: 2, 5:3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8};
                                               return mapping[tick];
                                          """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                   var mapping = {1: 27, 2: 28, 3: 29, 4: 1, 5:2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7};
                                                                   return mapping[tick];
                                                              """)
                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:

                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 27, 2: 28, 3: 29, 4: 30, 5:31, 6: 1, 7: 2, 8: 3, 9: 4, 10: 5};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 27, 2: 28, 3: 29, 4: 30, 5:1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6};
                                               return mapping[tick];
                                          """)
            if diaini == 28:
                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 28, 2: 1, 3: 2, 4: 3, 5:4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9};
                                               return mapping[tick];
                                          """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                   var mapping = {1: 28, 2: 29, 3: 1, 4: 2, 5:3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8};
                                                                   return mapping[tick];
                                                              """)
                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 28, 2: 29, 3: 30, 4: 31, 5:1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 28, 2: 29, 3: 30, 4: 1, 5:2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7};
                                               return mapping[tick];
                                          """)

            if diaini == 29:

                if mesini == 2:
                    if (date.today().year % 4) != 0:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 28, 2: 1, 3: 2, 4: 3, 5:4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9};
                                               return mapping[tick];
                                          """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                   var mapping = {1: 29, 2: 1, 3: 2, 4: 3, 5:4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9};
                                                                   return mapping[tick];
                                                              """)

                elif mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 29, 2: 30, 3: 31, 4: 1, 5:2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 29, 2: 30, 3: 1, 4: 2, 5:3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8};
                                               return mapping[tick];
                                          """)

            if diaini == 30:

                if mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 30, 2: 31, 3: 1, 4: 2, 5:3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 30, 2: 1, 3: 2, 4: 3, 5:4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9};
                                               return mapping[tick];
                                          """)

            if diaini == 31:
                if mesini == 1 or mesini == 3 or mesini == 5 or mesini == 8 or mesini == 10 or mesini == 12:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                   var mapping = {1: 31, 2: 1, 3: 2, 4: 3, 5:4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9};
                                   return mapping[tick];
                              """)
                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                           var mapping = {1: 1, 2: 2, 3: 3, 4: 4, 5:5, 6: 6, 7: 7, 8: 7, 9: 9, 10: 10};
                                           return mapping[tick];
                                      """)

        # EMOJI_EMB_VIZ_FILE = 'emoji_embeddings.csv'
        #
        #
        # df = pd.read_csv(EMOJI_EMB_VIZ_FILE)
        # a=df['emoji'][122]
        # b=df['emoji'][123]
        # c=df['emoji'][124]
        # d=df['emoji'][125]
        # e=df['emoji'][126]
        # f=df['emoji'][127]
        # g=df['emoji'][128]
        # h=df['emoji'][129]
        # k=df['emoji'][110]
        # l=df['emoji'][111]
        # m=df['emoji'][122]
        # n=df['emoji'][112]

        a = (emoji.emojize("\u26C8\uFE0F"))  # TROVOADA COM CHUVA
        b = (emoji.emojize("\U0001f327\uFE0F"))  # CHUVA
        # c=(emoji.emojize("\u26A1",))#trovoada
        c = (emoji.emojize("\U000026A1"))  # trovoada
        d = (emoji.emojize("\U0001f4a7"))  # chuvisco
        e = (emoji.emojize("\U0001f32b\uFE0F"))  # nevoeiro
        f = (emoji.emojize("\U0001f329\uFE0F"))  # trovoada isolada
        g = (emoji.emojize("\U0001f525"))  # fumaca
        h = (emoji.emojize("\U0001f7e8"))  # nevoa umida
        k = (emoji.emojize("\U0001f538"))  # nevoaseca
        l = (emoji.emojize("\U0001f329"))  # trovoada
        m = (emoji.emojize("\U0001f53d"))  # pancadas de chuva
        n = (emoji.emojize("\U0001f4dd"))  # pancadas de chuva
        o =  (emoji.emojize("\U0001f9ca"))  # granizo



        # pd.set_option('max_columns', None)
        #areatrab = 1  # dado entrada
        # datainicio='27/03/20'#dado entrada

        #datainicio = datetime.utcnow() - timedelta(9)
        datainicio = datainicio.strftime('%d/%m/%y')
        print('DATA INICIO')
        print(datainicio)

        if areatrab == 1:
          #  estacao_area = 'SBJR,SBES,SBME,SBCP,SBFS,SBRJ,SBCB,SBVT,SBPS,SBGL,SBNT,SBMS,SBAC,SBJE,SBPB,SNRU,SBAR,SBMO,SBRF,SBJP,SBSG,SBFZ,SBSL,SBTE,SBJU,SBKG,SBFN,SBPL,SBPJ'
            # estacao_area = 'SBFZ,'
            #arqi1 = pd.read_csv('metar_trat_teste1.csv')
            arqi1 = pd.read_csv('metar_trat_teste1.csv')
        else:

            #estacao_area = 'SBRD,SBVH,SWEI,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SWPI,SBTF,SBUA,SBEG,SBBV'  # sem SBMY SBCY
            # estacao_area = 'SBVH'
            # estacao_area ='SBEG,'
            #arqi1 = pd.read_csv('metar_trat_teste2.csv')
            arqi1 = pd.read_csv('metar_trat_teste2.csv')
        estacao_area=est
        noestacao = estacao_area.split(',')

        for i in range(0, 1, 1):
            try:
                print('nome da estação: ', noestacao[i])
                nome_estacao = noestacao[i]
                arqi = arqi1.loc[(arqi1['estacao'] == nome_estacao)]
                arqi = arqi.reset_index(drop=True)
               # print('arquivo: ', arqi)
               
                #cwd = os.getcwd()
                #if areatrab == 1:

                #    if os.path.isdir(cwd + '/tabuleiro/area1/'):
                #        caminho = cwd + '/tabuleiro/area1/'
                #    else:
                #        mkdir(cwd + '/tabuleiro/area1/')
                #        caminho = cwd + '/tabuleiro/area1/'
               # else:
                 #   if os.path.isdir(cwd + '/tabuleiro/area2/'):
                  #      caminho = cwd + '/tabuleiro/area2/'
                   # else:
                    #    mkdir(cwd + "/tabuleiro/area2/")
                   #     caminho = cwd + '/tabuleiro/area2/'
               # output_file((caminho + arqi['estacao'][0] + "tab.html"))

                # print(arqi)
                # result1= arqi.loc[(arqi['data_hora']>=datacomp)]

                x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in arqi.datahora]
                arqi['data_hora'] = x
                # datetime.day(x)

                ddata = arqi.data_hora
                diai = arqi['data_hora']
                especi = []
                especi.append('-')
                valores = []
                valores.append('60')
                stop = []
                stop.append('')
                noespec = []
                noespec.append('1')

                # pd.set_option('max_colwidht',70)
                for jj in range(0, len(diai), 1):
                    if jj > 0:
                        especi.append('-')
                        valores.append('')
                        stop.append('')
                        noespec.append('2')
                        iii = 1
                        maior = 0
                        # val=str(arqi.metar[jj])
                        if str(arqi.metar[jj]) == "nan":
                            valores[jj] = '0'
                        else:
                            valores[jj] = str(len(arqi.metar[jj]))
                        if (arqi.metar[jj] == "-"):
                            arqi.metar[jj] = arqi.speci[jj]
                            valorespec = str(len(arqi.speci[jj]))
                            valores[jj] = str(valorespec)

                        if diai[jj] == diai[jj - iii]:
                            stop[jj] = 'A'
                            while (diai[jj] == diai[jj - iii]):
                                arqi.metar[jj - iii] = str(arqi.metar[jj - iii]) + '\n' + str(arqi.speci[jj])
                                # valores[jj] = str(len(arqi.metar[jj-iii]))
                                valorespec = str(len(arqi.speci[jj]))
                                # valores[jj]=str(len(arqi.metar[jj]))
                                if int(valores[jj - iii]) < int(valorespec):
                                    valores[jj - iii] = str(valorespec)
                                especi[jj - iii] = (arqi.metar[jj - iii])
                                noespec[jj - iii] = str(iii + 1)
                                stop[jj - iii] = 'A'
                                # valores[jj-iii]=especi[jj-iii].split('=')
                                iii = iii + 1
                                if (jj-iii) < 0:
                                    break
                            # noespec[jj-iii] = str(iii+2)
                        #
                        #
                        else:
                            if len(str(arqi['speci'][jj])) >10:
                                stop[jj] = 'A'
                            else:
                                noespec[jj]='1'

                        #         especi.append('-')
                # arqi['especial'] = arqi['especi'].str[:10]

                # arqi['especial']=especi
                arqi['valor'] = valores
                arqi['aviso'] = stop
                arqi['nspc'] = noespec
                
                #print(valores)
                # arqi['especial'] = arqi['especial'].str[:50]
                # arqi = arqi.reset_index(drop=True)

                arqi = arqi.drop_duplicates(['estacao', 'datahora'])

                ano = diai[0].year
                mes = diai[0].month

                diaini = int(datainicio[0:2])
                mesini = int(datainicio[3:5])
                diafim = diaini + 10
                datafim = str(diafim) + '/' + datainicio[3:5] + '/' + datainicio[6:10]
                date_inicio = datetime.strptime(datainicio, '%d/%m/%y')
                date_fim = date_inicio + timedelta(days=10)

                mes_ini = str(date_inicio.month)
                dia_ini = str(date_inicio.day)
                ano_ini = str(date_inicio.year)

                mes_fim = str(date_fim.month)
                # datafim =1
                if date_fim.day == 1 and (
                        date_fim.month == 4 or date_fim.month == 6 or date_fim.month == 8 or date_fim.month == 9 or date_fim.month == 11 or date_fim.month == 1):
                    dia_fim = '31'
                    mes_fim = str(date_fim.month - 1)
                    ano_fim = str(date_fim.year)
                    if str(date_fim.month - 1) == '0':
                        mes_fim = '12'
                        ano_fim = str(date_fim.year - 1)
                elif date_fim.day == 1:
                    if date_fim.month==3:
                        if date_fim.year%4==0:
                            dia_fim = '29'
                            mes_fim = str(date_fim.month - 1)
                            ano_fim = str(date_fim.year)
                        else:
                            dia_fim = '28'
                            mes_fim = str(date_fim.month - 1)
                            ano_fim = str(date_fim.year)
                    else:
                        dia_fim = '30'
                        mes_fim = str(date_fim.month - 1)
                        ano_fim = str(date_fim.year)

                
                else:
                    dia_fim = str(date_fim.day- 1)
                    #dia_fim = str(date_fim.day)
                    ano_fim = str(date_fim.year)

                datatit = dia_ini + '/' + mes_ini + '/' + ano_ini + ' a ' + dia_fim + '/' + mes_fim + '/' + ano_fim
                arqi = arqi.loc[(arqi['data_hora'] >= date_inicio)]
                arqi = arqi.loc[(arqi['data_hora'] < date_fim)]
                arqi.sort_values(by=['estacao', 'data_hora'], inplace=True)
                arqi = arqi.reset_index(drop=True)
               # print('CHEGUEI AQUI')
                dia = []
                hora = []
                diai = arqi['data_hora']
                deltatempo = diafim - 11
                ent = 0
                j = 0
                entrar = False
                for i in range(0, len(diai)):

                    if (diai[i].day - deltatempo) < 0:
                        j = j + 1
                        #     ent=ent+1diai[i].day

                        if mesini == 2 and (diai[i].day == 1) and (diai[i - j].day != 28):

                            dia.append(29 - deltatempo+1)
                            hora.append(diai[i].hour)

                            ult = dia[i] - 1
                            entrar = True
                        else:
                            if entrar == True:
                                ult = diai[i].day
                                entrar = True
                            if mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
                                ult = 32
                            elif mesini == 4 or mesini == 6 or mesini == 9 or mesini == 11:
                                ult = 31
                            elif mesini == 2 and int(ano_ini) % 4 == 0:
                                ult = 30
                            elif mesini == 2 and int(ano_ini) % 4 != 0:
                                ult = 29

                            dia.append(diai[i].day + ult - diaini)
                            hora.append(diai[i].hour)

                    else:

                        dia.append(diai[i].day - deltatempo)
                        hora.append(diai[i].hour)
                        ult = diai[i].day + 1
                #    print(arqi.vis[34])
                arqi['diaa'] = dia
                print('dia: ', dia)
                arqi['group'] = dia
                arqi['period'] = (hora)
                ddi = (arqi.data_hora[0]).day
                ddf = (arqi.data_hora[len(arqi.datahora) - 1]).day
                periods = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17",
                           "18", "19", "20", "21", "22", "23"]
                periodos = arqi.period[1:23]
                groups = [str(x) for x in range(1, 12)]
                # print('groups, ',groups[9])
                # print(arqi.period)
                arqi["period"] = [periods[x] for x in arqi.period]
                # print(len(arqi['period']))

                ###temp max e min diaria
                #######arqi.groupby(by=arqi['data_hora'].dt.day).agg({'dryt': 'max'})
                #######arqi.groupby(by=arqi['data_hora'].dt.day).agg({'dryt': 'min'})
                # df = elements.copy()

                # arqi["dryt"] = arqi["vis"].astype(str)/10
                # arqi["vis"] = arqi["vis"].astype(round)
                arqi['vis'] = arqi['vis'].astype(np.float32)
                arqi["vis"] = round(arqi.vis / 100, 0)

                arqi["diaa"] = arqi["diaa"].astype(str)

                # tratamento tempo presente
                arqi['tpb'] = arqi['tp']
                arqi['tp'].fillna('', inplace=True)

                # arqi['dryt'].fillna('xx', inplace=True)
                # arqi['dewp'].fillna('xx', inplace=True)
                # umidade relativa
                ur = []
                tmax = []
                tmin = []
                #vmax = []
               # vmin = []
                arqi['drytt'] = arqi['dryt']
                arqi['drytt'].fillna(0, inplace=True)
                arqi['dewpt'] = arqi['dewp']
                # arqi['dewp'] = arqi['dewp'].fillna(0).astype(int)
                arqi['datahora2'] = arqi['data_hora']
                ccmax = arqi.groupby(pd.Grouper(key='data_hora', axis=0, freq='1D', sort=True)).max()
                ccmin = arqi.groupby(pd.Grouper(key='data_hora', axis=0, freq='1D', sort=True)).min()

                for bbb in range(0, len(ccmax['datahora2'])):
                    for bb in range(0, len(arqi['datahora2']), 1):
                        if ccmax['datahora2'].dt.day[bbb] == arqi['datahora2'].dt.day[bb]:
                            tmax.append(ccmax.drytt[bbb])
                            tmin.append(ccmin.drytt[bbb])
                           # vmax.append(ccmax.wspd[bbb])
                           # vmin.append(ccmin.wspd[bbb])

                arqi['tmax'] = tmax
                arqi['tmin'] = tmin
               # arqi['vmax'] = vmax
               # arqi['vmin'] = vmin

                arqi['dewpt'].fillna(0, inplace=True)
                dewttt = []
                attt = []
                # arqi['ur'] = mpcalc.relative_humidity_from_dewpoint(arqi['dryt'] * units.degC, arqi['dewp'] * units.degC).magnitude * 100
                for iur in range(0, len(arqi['dryt']), 1):

                    if str(arqi.dewpt[iur])[0:1] == 'M':
                        atb = np.ceil(float(arqi.dewpt[iur][1:2]))

                    else:
                        atb = np.ceil(float(arqi.dewpt[iur]))
                    at = float((arqi.drytt[iur]))
                    if arqi.dewpt[iur] == 0:
                        attt.append('xx')

                    else:
                        attt.append(np.ceil(float(arqi.dewpt[iur])))
                    dewttt.append(atb)

                    if (arqi['dewp'][iur]) != (arqi['dewp'][iur]):
                        ur.append('-')
                    else:
                        # uuu = (
                        # round(mpcalc.relative_humidity_from_dewpoint(at * units.degC, atb * units.degC).magnitude * 100), 0)
                        # ur.append(uuu)
                        if at < atb:
                            ur.append('-')
                        else:
                            uuu = umidade(at,atb)
                            ur.append(int(uuu))
                #     if at == 0 or atb==0:
                #         ur.append('NaN')
                #     else:
                #         at=int(at)
                #         atb=int(atb)
                #         if at < atb:
                #             ur.append(int('0'))
                #         else:
                #             if at >= 0:
                #                 aa = 7.5 * at / (237.5 + at)
                #             else:
                #                 aa = 9.5 * at / (265.5 + at)
                #             u_b = 7.5 * atb
                #             cc = 237.3 + atb
                #             dd = ((-aa * cc) + u_b) / cc
                #             ur.append(int(10**(dd)*100))
                #
                #         if int(ur[iur]) > 100:
                #             ur[iur] = 100
                #
                #
                arqi['de'] = attt
                arqi['de'].fillna('xx', inplace=True)
                arqi['dewpp'] = dewttt
                arqi['ur'] = ur
                arqi['ur'].fillna('xx', inplace=True)
                arqi['ur'] = arqi['ur'].replace([0], 'NaN')
                arqi['dryt'].fillna('xx', inplace=True)
                arqi['dewp'].fillna('xx', inplace=True)

                arqi['tp'] = arqi['tp'].replace(['-TSRA'], '-' + a)
                arqi['tp'] = arqi['tp'].replace(['+TSRA'], '+' + a)
                arqi['tp'] = arqi['tp'].replace(['TSRA'], a)
                arqi['tp'] = arqi['tp'].replace(['-RA'], '-' + b)
                arqi['tp'] = arqi['tp'].replace(['RA'], b)
                arqi['tp'] = arqi['tp'].replace(['+RA'], '+' + b)
                arqi['tp'] = arqi['tp'].replace(['RADZ'], b)
                arqi['tp'] = arqi['tp'].replace(['-RADZ'], '-' + b)
                arqi['tp'] = arqi['tp'].replace(['+RADZ'], '+' + b)
                arqi['tp'] = arqi['tp'].replace(['VCTS'], c)
                arqi['tp'] = arqi['tp'].replace(['TS'], l)
                arqi['tp'] = arqi['tp'].replace(['DZ'], d)
                arqi['tp'] = arqi['tp'].replace(['FZDZ'], d)
                arqi['tp'] = arqi['tp'].replace(['-DZ'], "-" + d)
                arqi['tp'] = arqi['tp'].replace(['+DZ'], "+" + d)
                arqi['tp'] = arqi['tp'].replace(['FU'], g)
                arqi['tp'] = arqi['tp'].replace(['FG'], e)
                arqi['tp'] = arqi['tp'].replace(['VCFG'], e)
                arqi['tp'] = arqi['tp'].replace(['PRFG'], e)
                arqi['tp'] = arqi['tp'].replace(['BCFG'], e)
                arqi['tp'] = arqi['tp'].replace(['MIFG'], e)
                arqi['tp'] = arqi['tp'].replace(['FZFG'], e)
                arqi['tp'] = arqi['tp'].replace(['BR'], h)
                arqi['tp'] = arqi['tp'].replace(['HZ'], k)
                arqi['tp'] = arqi['tp'].replace(['VCSH'], ').(')
                arqi['tp'] = arqi['tp'].replace(['-SHRA'], "-" + m)
                arqi['tp'] = arqi['tp'].replace(['+SHRA'], "+" + m)
                arqi['tp'] = arqi['tp'].replace(['SHRA'], m)
                arqi['tp'] = arqi['tp'].replace(['+TSGRRA'],"+" + o)
                arqi['tp'] = arqi['tp'].replace(['TSGRRA'],o)
                arqi['tp'] = arqi['tp'].replace(['-TSGRRA'],"-"+o)
                arqi['aviso'] = arqi['aviso'].replace(['A'], n)
                # fim

                # tratamento rajada
                arqi['gust'].fillna('', inplace=True)
                auxgust = []
                for igust in range(0, len(arqi['gust']), 1):
                    if int(arqi['gust'][igust] != 0):

                        auxgust.append('G' + str(arqi['gust'][igust]))
                        auxgust[igust] = auxgust[igust][0:3]
                    else:
                        auxgust[igust] = '0'
                arqi['gust'] = auxgust[:]
                arqi['gust'].mask(arqi['gust'] == 'G', '', inplace=True)
                # fim rajada
                # vento
                arqi['wdir'].fillna(0, inplace=True)

                # print(arqi['wdir'])
                # tratando a camada de nuvens 1
                # inicio-----------------
                auxaltn1 = []
                auxqn1 = []
                arqi['qn1'].fillna("", inplace=True)
                arqi['altn1'].fillna('', inplace=True)
                for inuv in range(0, len(arqi['altn1']), 1):
                    if len(str(arqi['altn1'][inuv])) < 5:
                        auxaltn1.append('0' + str(arqi['altn1'][inuv]))
                        auxaltn1[inuv] = auxaltn1[inuv][0:3]
                    else:
                        auxaltn1.append(str(arqi['altn1'][inuv]))
                        auxaltn1[inuv] = auxaltn1[inuv][0:3]

                    auxqn1.append((arqi['qn1'][inuv]))

                arqi['altn1'] = auxaltn1[:]

                # arqi['altn1'].mask(arqi['altn1'] == '010', '100', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '0', '', inplace=True)
                # print(auxaltn1[:])

                arqi['altn1'].mask(arqi['altn1'] == '09', '009', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '08', '008', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '07', '007', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '06', '006', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '05', '005', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '04', '004', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '03', '003', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '02', '002', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '01', '001', inplace=True)

                arqi['altn1'].mask(arqi['altn1'] == '09.', '009', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '08.', '008', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '07.', '007', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '06.', '006', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '05.', '005', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '04.', '004', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '03.', '003', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '02.', '002', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '01.', '001', inplace=True)
                arqi['altn1'].mask(arqi['altn1'] == '00.', '000', inplace=True)

                # fim------------------

                # tratando a camada de nuvens 2
                # inicio-----------------
                auxaltn2 = []

                arqi['altn2'].fillna('', inplace=True)
                for inuv in range(0, len(arqi['altn2']), 1):
                    if inuv == 24:
                        GGGGGGGGGG = 2
                    auxaltn2.append('0' + str(arqi['altn2'][inuv]))
                    if len(auxaltn2[inuv]) == 6:
                        auxaltn2[inuv] = auxaltn2[inuv][1:4]
                    else:
                        auxaltn2[inuv] = auxaltn2[inuv][0:3]

                arqi['altn2'] = auxaltn2[:]
                # arqi['altn2'].mask(arqi['altn2'] == '010', '100', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '0', '', inplace=True)
                # print(auxaltn2[:])
                arqi['qn2'].fillna("", inplace=True)

                arqi['altn2'].mask(arqi['altn2'] == '09', '009', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '08', '008', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '07', '007', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '06', '006', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '05', '005', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '04', '004', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '03', '003', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '02', '002', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '01', '001', inplace=True)

                arqi['altn2'].mask(arqi['altn2'] == '09.', '009', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '08.', '008', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '07.', '007', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '06.', '006', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '05.', '005', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '04.', '004', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '03.', '003', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '02.', '002', inplace=True)
                arqi['altn2'].mask(arqi['altn2'] == '01.', '001', inplace=True)
                # fim------------------

                # arqi["altnb"]='0'+arqi["altn1"]
                # tratando a camada de nuvens cb
                # inicio-----------------
                auxaltncb = []

                arqi['altncb'].fillna('', inplace=True)
                for inuv in range(0, len(arqi['altncb']), 1):
                    auxaltncb.append(str(arqi['altncb'][inuv]))
                    if str(auxaltncb[inuv][-1:]) != 'T':
                        auxaltncb[inuv] = auxaltncb[inuv][0:3] + 'CB'
                arqi['altncb'] = auxaltncb[:]
                arqi['altncb'].mask(arqi['altncb'] == 'CB', '', inplace=True)
                # (auxaltn2[:])
                arqi['qncb'].fillna('', inplace=True)

                # fim------------------
                # colocando a direção 19/01
                # arqi["wdiwdir"] = arqi["wdir"].astype(str)
                wdirwdir = []

                for iwdir in range(0, len(arqi['wdir']), 1):
                    auxwdir = str(arqi.wdir[iwdir])
                    if auxwdir == 'VRB':
                        FFFF = 1
                    if arqi.wdir[iwdir] < 100:
                        if ("VRB" in str(arqi.metar[iwdir][0:30])):
                            wdirwdir.append('VRB')
                        else:
                            wdirwdir.append('0' + auxwdir[0:1])
                    else:
                        wdirwdir.append(auxwdir[0:2])
                arqi["wdirstr"] = wdirwdir

                # tratamento nuvem

                qn1qn1 = []
                # qn1
                # altn1
                for ialt1 in range(0, len(arqi['altn1']), 1):
                    auxalt1 = (arqi.altn1[ialt1])
                    auxauxqn1 = str(arqi.qn1[ialt1])
                    #if arqi['metar'][ialt1].find('VV00') > -1:
                    if auxauxqn1=='OVC':
                        if arqi['metar'][ialt1].find('VV00') > -1:
                            if arqi['metar'][ialt1].find('VV00') and  arqi['metar'][ialt1].find('SPECI')==-1:
                    #if auxalt1 == '000':
        
                                qn1qn1.append('  VV')
                            elif  (arqi['metar'][ialt1].find('OVC') >-1) and (arqi['metar'][ialt1].find('OVC') <  arqi['metar'][ialt1].find('VV00')):
        
                                qn1qn1.append(auxauxqn1)
                            else:
                                qn1qn1.append('  VV')
                        else:
                            qn1qn1.append(auxauxqn1)
                    else:
                        # alt1alt1.append(auxalt1)
                        qn1qn1.append(auxauxqn1)
        
                # arqi["alt1"] = alt1alt1
                auxqn1 = qn1qn1
                # colocando a direçãof
                # tratando a VISIBILIDADE
                # inicio-----------------
                auxvis = []

                arqi['vis'].fillna(-9999.0, inplace=True)
                for inuv in range(0, len(arqi['vis']), 1):

                    if arqi['vis'][inuv] == 100:
                        arqi['vis'][inuv] = 99

                    if int(arqi['vis'][inuv]) < 0:
                        auxvis.append('XX')
                    elif arqi['vis'][inuv] < 10:

                        auxvis.append('0' + str(arqi['vis'][inuv]))
                    else:
                        auxvis.append(str(arqi['vis'][inuv]))
                    auxvis[inuv] = auxvis[inuv][0:2]
                    if int(arqi['vis'][inuv]) == 99 and arqi['qn1'][inuv] == "" and arqi['tp'][inuv] == "" and arqi['qncb'][
                        inuv] == "":
                        auxvis[inuv] = 'CVK'
                    if int(arqi['vis'][inuv]) != 99 and arqi['qn1'][inuv] == ""and arqi['tp'][inuv] == ""and arqi['qncb'][
                        inuv] == "":
                        
                        auxqn1[inuv] = 'NSC'
                        # arqi['qn1'][inuv].mask(arqi['qn1'][inuv] == "", 'NSC', inplace=True)
                    if int(arqi['vis'][inuv]) == 99 and arqi['qn1'][inuv] == "" and arqi['tp'][inuv]!="" and arqi['qncb'][
                        inuv] == "":
                        auxqn1[inuv]='NSC'
                arqi['qn1'] = auxqn1[:]
                arqi['qn1'].mask(arqi['qn1'] == '0', '', inplace=True)
                arqi['vis'] = auxvis[:]
                auxmetar = []
                # for u in range(0,len(arqi['metar']),1):
                #     pmetar= arqi.metar[u].split("=")
                #     auxmetar.append(pmetar)
                # from bokeh.models import HoverTool
                # Tooltips = [
                #         ("Estação", "@estacao"),
                #         ("Data hora", "@datahora"),
                #         # ("Temp. do ar:", "@{dryt}ºC"),
                #         # ("Int. vento", "@{wspd}kt"),
                #         # ("Direção vento", "@{wdir}" ),
                #         # ("Tempo presente ", "@{tpb}"),
                #         ("UR", "@{ur}%"),
                #         ("Metar/Speci", "@{metar}" )
                #         #("Speci", "@{metar}")
                #         # '{:>10}'.format('test')
                #         # '$@{adj close}{%0.2f}'
                #      #   ("CPK color", "$color[hex, swatch]:CPK"),
                #        ]
                Tooltips = """
               <div>
                <font color = "red"
                <i><b>Estação: </i>  @estacao</tr> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  Datahora: @datahora&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp  UR: @ur%
                &nbsp&nbsp&nbsp&nbsp Tmáx: @tmax°C&nbsp&nbsp Tmin: @tmin°C&nbsp&nbsp </b>
                </font>
                <div>
    
    
                <textarea cols=@valor rows=@nspc wrap="hard">@metar</textarea>
    
    
    
                """

                # TOOLTIPS = """
                # <div>
                #     <div>
                #         <img
                #             src="@arqi" height="100" alt="@metar" width="450"
                #             style="float: left; margin: 0px 15px 15px 0px;"
                #
                #         ></img>
                #     </div>
                #
                # &nbsp&nbsp Vmax: @vmax kt&nbsp&nbsp Vmin: @vmin kt
                #
                # </div>
                # """

                # p = figure(title="Tabuleiro: "+arqi.estacao[0]+' '+datatit, plot_width=1500, plot_height=2300,
                #            x_range=groups, y_range=list(reversed(periods)),x_axis_location="above",
                #            toolbar_location=None, tooltips=TOOLTIPS,border_fill_color='gray',background_fill_color='gray',)
                p = figure(title="Tabuleiro: " + arqi.estacao[0] + ' ' + datatit, width=1500, height=2300,
                           x_range=groups, y_range=list(reversed(periods)), x_axis_location="above",
                           toolbar_location=None, tooltips=Tooltips)
                

                # p.add_layout(
                #     BoxAnnotation(left='starttime', right='enddtime', bottom='startvalue', source=arqi, fill_color='green',
                #                   fill_alpha=0.3))
                p.title.align = "center"
                p.title.text_color = "orange"
                p.title.text_font_size = "30px"
                p.title.background_fill_color = "black"
                p.xaxis.major_label_orientation = "horizontal"

                # p.xaxis.ticker = [1,2,3,4,5,6,7,8,9,10]
                #
                # p.xaxis.major_label_overrides = {1: '07', 2: 'B', 3: 'C',4: 'A', 5: 'B', 6: 'C',7: 'A', 8: 'B', 9: 'C', 10: 'C'}
                # #p.xaxis.ticker = [1, 2, 3]
                formata()
                # p.xaxis.ticker = FixedTicker(ticks=[0, 3, 6, 9])
                # p.xaxis[0].ticker = FixedTicker(ticks=majorticks)
                p.xaxis.axis_label_text_font_size = "20pt"
                p.yaxis.axis_label_text_font_size = "20pt"
                p.xaxis.axis_label = 'D I A'
                p.yaxis.axis_label = 'H O R A  (UTC)'
                p.x_range.range_padding = -0.07
                # p.xaxis.major_label_orientation = 1.3

                p.xgrid.grid_line_color = "#aaaaee"

                # arqi['diaaa'].mask(arqi['diaa'] == "0", "24", inplace=True)
                # arqi["diaaaa"] = arqi["diaaa"].astype(int)

                # print(arqi.diaaaa)
                # arqi.loc[(arqi.period == '00'),'period']='24'
                arqi["periodd"] = arqi["period"].astype(int)

                xx = arqi["group"]
                yy = arqi["period"]
                u = np.sin(np.pi / 180 * arqi.wdir[:])
                v = np.cos(np.pi / 180 * arqi.wdir[:])

                cm = np.array(["#C7E9B4", "#7FCDBB", "#41B6C4", "#1D91C0", "#225EA8", "#0C2C84"])
                # ix = ((length-length.min())/(length.max()-length.min())*5).astype('int')
                # colors = cm[ix]

                # x_text_font_size = "40px"

                # print(arqi.group)
                r = p.rect("group", "period", width=1.0, height=1, source=arqi, fill_alpha=0.6)  # , legend_field="dryt")
                # #              color=factor_cmap('metal', palette=list(cmap.values()), factors=list(cmap.keys())))
                # #

                text_props = {"source": arqi, "text_align": "left", "text_baseline": "middle"}
                #
                x = dodge("group", -0.4, range=p.x_range)
                y = dodge("period", -0.8, range=p.y_range)

                #
                # p.text(x=x, y="period", text="dryt", text_font_style="bold", **text_props)
                #
                # p.circle(x=x, y=dodge("period", 0.3, range=p.y_range),   size=10, color="navy", alpha=0.5)
                # p.circle_x(x,y="period")

                p.circle(arqi["group"], arqi["period"],
                         color='black', fill_alpha=0.4, size=10)

                # p.ellipse(arqi["group"], arqi["period"], width=0.1, height=0.0,
                #           angle=0.8, color="red")

                # p.circle([1, 2, 3, 4, 5,6, 7, 8, 9, 10], [1, 2, 3, 4, 5,6, 7, 8, 9, 10], size=10, color="navy", alpha=0.5)
                p.text(x=x, y=dodge("period", 0.3, range=p.y_range), text="dryt", text_font_style="bold",
                       text_font_size="11px", **text_props)

                p.text(x=dodge("group", -0.07, range=p.x_range), y=dodge("period", 0.3, range=p.y_range), text="aviso",
                       text_font_style="bold",
                       text_font_size="11px", **text_props)

                # print(x)

                p.text(x=x, y=dodge("period", -0.35, range=p.y_range), text="de", text_font_style="bold",
                       text_font_size="11px", **text_props)
                p.text(x=x, y=dodge("period", -0.05, range=p.y_range), text="vis", text_font_style="bold",
                       text_font_size="11px", **text_props)
                p.text(x=dodge("group", -0.3, range=p.x_range), y=dodge("period", 0.05, range=p.y_range), text="tp",
                       text_font_style="bold",
                       text_font_size="18px", text_color='red', **text_props)
                p.text(x=dodge("group", 0.3, range=p.x_range), y=dodge("period", 0.3, range=p.y_range), text="pres",
                       text_font_style="bold",
                       text_font_size="11px", **text_props)

                p.text(x=dodge("group", -0.07, range=p.x_range), y=dodge("period", -0.4, range=p.y_range), text="qn1",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)
                p.text(x=dodge("group", 0.065, range=p.x_range), y=dodge("period", -0.4, range=p.y_range), text="altn1",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)

                p.text(x=dodge("group", -0.07, range=p.x_range), y=dodge("period", -0.2, range=p.y_range), text="qn2",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)
                p.text(x=dodge("group", 0.065, range=p.x_range), y=dodge("period", -0.2, range=p.y_range), text="altn2",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)

                p.text(x=dodge("group", 0.07, range=p.x_range), y=dodge("period", -0.3, range=p.y_range), text="qncb",
                       text_font_style="bold", text_color='red',
                       text_font_size="9px", **text_props)
                p.text(x=dodge("group", 0.20, range=p.x_range), y=dodge("period", -0.3, range=p.y_range), text="altncb",
                       text_font_style="bold", text_color='red',
                       text_font_size="9px", **text_props)

                p.text(x=dodge("group", 0.06, range=p.x_range), y=dodge("period", -0.05, range=p.y_range), text="gust",
                       text_font_style="bold", text_color='red',
                       text_font_size="9px", **text_props)

                # -----dia 19
                p.text(x=dodge("group", 0.06, range=p.x_range), y=dodge("period", 0.1, range=p.y_range), text="wdirstr",
                       text_font_style="bold", text_color='black',
                       text_font_size="9px", **text_props)
                #### Intensidade do vento
                p.text(x=dodge("group", 0.4, range=p.x_range), y=dodge("period", -0.35, range=p.y_range), text="wspd",
                       text_font_style="bold", text_color='red',
                       text_font_size="11px", **text_props)
                #### Intensidade do vento - fim
                # -----dia 19
                # arqi['gust']=arqi['tp'].replace(['G'], g)
                # p.text(x=dodge("group",-0.09, range=p.x_range), y=dodge("period", -0.15, range=p.y_range), text="gust",text_font_style="bold",text_color='red',
                #         text_font_size="9px", **text_props)

                # p.text(x=["3", "3"], y=["VI", "VII"], text=["LA", "AC"], text_align="center", text_baseline="middle")

                # print(arqi.group)
                # print(arqi.periodd)

                yyy = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5,
                       18.5, 19.5, 20.5, 21.5, 22.5, 23.5]
                yyyyyy = [0.8, 1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8, 10.8, 11.8, 12.8, 13.8, 14.8, 15.8, 16.8, 17.8,
                          18.8, 19.8, 20.8, 21.8, 22.8, 23.8]
                xxx = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                xxxxxx = [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1,
                          1.1, 1.1, 1.1, 1.1, 1.1]
                # yyy=[11.5,12.5,13.5,14.5,15.5,16.5,17.5,18.5,19.5,20.5,21.5,22.5,23.5]
                # yyyyyy=[11.8,12.8,13.8,14.8,15.8,16.8,17.8,18.8,19.8,20.8,21.8,22.8,23.8]
                # xxx=[1,1,1,1,1,1,1,1,1,1,1,1,1]
                # xxxxxx=[1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1]

                # diacomp=[22,23,24,25,26,27,28,29,30,1]

                iwdir = -1
                idia = 0
                idiaa = -1
                ihora = 0

                for gg in range(0, 12, 1):
                    diaok = False
                    yyyy = []
                    xxxx = [i * gg for i in xxx]
                    for iii in range(len(yyy) - 1, -1, -1):
                        yyyy.append(yyy[iii])
                    for idi in range(0, len(dia), 1):
                        if gg == dia[idi]:
                            diaok = True

                    xxxxx = []
                    yyyyy = []
                    xxxxxx = []
                    yyyyyy = []
                    x0 = dia
                    y0 = hora
                    aux = -1
                    x7 = []
                    y7 = []
                    x8 = []
                    y8 = []
                    y9 = []
                    x9 = []
                    x10 = []
                    y10 = []
                    x11 = []
                    y11 = []
                    x12 = []
                    y12 = []
                    x13 = []
                    y13 = []
                    auxhorai = y0[0]
                    auxhoraf = y0[len(y0) - 1]

                    idiaa = idiaa + 1

                    # for ggg in range(0,24,1):

                    for ggg in range(0, 24, 1):
                        # print (dia[idiaa])
                        # print((dia[idia]))

                        if len(hora) != iwdir + 1:
                            if hora[ihora] == 12:
                                print(idia)

                            if hora[ihora] == ggg and diaok == True:
                                ihora = ihora + 1

                                # yyyy=  [i * 1 for i in yyy]
                                iwdir = iwdir + 1
                                idia = idia + 1
                                # print(dia[iwdir])
                                if xxxx[gg] != arqi.group[iwdir]:
                                    break
                                # print(iwdir)

                                if arqi.wdir[iwdir] != 0:

                                    # xxxxx.append(xxxx[gg] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                    # yyyyy.append(yyyy[ggg] + 0.25 * np.cos(np.pi/180*(arqi.wdir[iwdir])))
                                    aux = aux + 1
                                    # print(gg)
                                    # print((gg))

                                    # if arqi.wdir[iwdir]==90:
                                    #
                                    #     xxxxx.append(xxxx[gg] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                    #     yyyyy.append(yyyy[ggg] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                    #
                                    # else:

                                    xxxxx.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                    yyyyy.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))

                                    if arqi.wspd[iwdir] <= 2:

                                        if gg == 9:
                                            if ggg == 14:
                                                car = 55
                                        x7.append(xxxx[gg] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))

                                        xxxxxx.append((xxxxx[aux] + 0 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        yyyyyy.append((yyyyy[aux] + 0 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x8.append((xxxx[gg]))
                                        y8.append((yyyy[ggg]))
                                        x9.append((xxxx[gg]))
                                        y9.append((yyyy[ggg]))
                                        x10.append((xxxx[gg]))
                                        y10.append((yyyy[ggg]))
                                        x11.append((xxxx[gg]))
                                        y11.append((yyyy[ggg]))
                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))



                                    elif arqi.wspd[iwdir] <= 7:
                                        # if gg==9:
                                        #     if ggg==14:
                                        #         car=55
                                        x7.append(xxxx[gg] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))

                                        xxxxxx.append((xxxxx[aux] + 0.10 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.10 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        x8.append((xxxx[gg]))
                                        y8.append((yyyy[ggg]))
                                        x9.append((xxxx[gg]))
                                        y9.append((yyyy[ggg]))
                                        x10.append((xxxx[gg]))
                                        y10.append((yyyy[ggg]))
                                        x11.append((xxxx[gg]))
                                        y11.append((yyyy[ggg]))
                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))



                                    elif arqi.wspd[iwdir] > 7 and arqi.wspd[iwdir] <= 12:

                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append((xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        x8.append((xxxx[gg]))
                                        y8.append((yyyy[ggg]))
                                        x9.append((xxxx[gg]))
                                        y9.append((yyyy[ggg]))
                                        x10.append((xxxx[gg]))
                                        y10.append((yyyy[ggg]))
                                        x11.append((xxxx[gg]))
                                        y11.append((yyyy[ggg]))
                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))

                                    elif arqi.wspd[iwdir] > 12 and arqi.wspd[iwdir] <= 17:

                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append((xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append((xxxxx[aux] + 0.1 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y9.append((yyyyy[aux] + 0.1 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        x10.append((xxxx[gg]))
                                        y10.append((yyyy[ggg]))
                                        x11.append((xxxx[gg]))
                                        y11.append((yyyy[ggg]))
                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))
                                    elif arqi.wspd[iwdir] > 17 and arqi.wspd[iwdir] <= 22:

                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append((xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append((xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append((yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        x10.append((xxxx[gg]))
                                        y10.append((yyyy[ggg]))
                                        x11.append((xxxx[gg]))
                                        y11.append((yyyy[ggg]))
                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))
                                    elif arqi.wspd[iwdir] > 22 and arqi.wspd[iwdir] <= 27:
                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append((xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append((xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append((yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append((xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append((yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.15 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 135))))
                                        y11.append((yyyyy[aux] + 0.15 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 135))))
                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))
                                    elif arqi.wspd[iwdir] > 27 and arqi.wspd[iwdir] <= 32:
                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append((xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append((xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append((yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append((xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append((yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.21 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y11.append((yyyyy[aux] + 0.21 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 120))))

                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))
                                    elif arqi.wspd[iwdir] > 32 and arqi.wspd[iwdir] <= 37:
                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append((xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append((xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append((yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append((xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append((yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.21 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y11.append((yyyyy[aux] + 0.21 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 120))))

                                        x12.append((xxxx[aux] + 0.15 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y12.append((yyyy[aux] + 0.15 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x13.append((xxxxx[aux] + 0.19 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 145))))
                                        y13.append((yyyyy[aux] + 0.19 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 145))))
                                    elif arqi.wspd[iwdir] > 37 and arqi.wspd[iwdir] <= 42:
                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append((xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append((yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append((xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append((yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append((xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append((yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.21 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y11.append((yyyyy[aux] + 0.21 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 120))))

                                        x12.append((xxxx[aux] + 0.15 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y12.append((yyyy[aux] + 0.15 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x13.append((xxxxx[aux] + 0.24 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 130))))
                                        y13.append((yyyyy[aux] + 0.24 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 130))))


                                else:
                                    xxxxx.append(xxxx[gg])
                                    yyyyy.append(yyyy[ggg])
                                    x7.append((xxxx[gg]))
                                    y7.append((yyyy[ggg]))
                                    x8.append((xxxx[gg]))
                                    y8.append((yyyy[ggg]))
                                    x9.append((xxxx[gg]))
                                    y9.append((yyyy[ggg]))
                                    x10.append((xxxx[gg]))
                                    y10.append((yyyy[ggg]))
                                    x11.append((xxxx[gg]))
                                    y11.append((yyyy[ggg]))
                                    x12.append((xxxx[gg]))
                                    y12.append((yyyy[ggg]))
                                    x13.append((xxxx[gg]))
                                    y13.append((yyyy[ggg]))
                                    aux = aux + 1
                                    xxxxxx.append((xxxxx[aux]))
                                    yyyyyy.append((yyyyy[aux]))
                                    p.circle(xxxx[gg], yyyy[ggg],
                                             color='black', fill_alpha=0.2, size=20)
                            else:
                                xxxxx.append(xxxx[gg])
                                yyyyy.append(yyyy[ggg])
                                p.circle(xxxx[gg], yyyy[ggg],
                                         color='black', fill_alpha=0.2, size=20)
                                aux = aux + 1
                        else:

                            xxxxx.append(xxxx[gg])
                            yyyyy.append(yyyy[ggg])
                            p.circle(xxxx[gg], yyyy[ggg],
                                     color='black', fill_alpha=0.2, size=20)
                            aux = aux + 1
                        # #imprime a direção
                    p.segment(x0=xxxx[gg], y0=yyyy, x1=xxxxx, y1=yyyyy, color="black", line_width=1)

                    # imprime as barbelas
                    p.segment(x0=x7, y0=y7, x1=xxxxxx, y1=yyyyyy, color="black", line_width=1)
                    p.segment(x0=x8, y0=y8, x1=x9, y1=y9, color="black", line_width=1)
                    p.segment(x0=x10, y0=y10, x1=x11, y1=y11, color="black", line_width=1)
                    p.segment(x0=x12, y0=y12, x1=x13, y1=y13, color="black", line_width=1)

                    # p.text(x=["4"], y=["23"], text=["LA"], text_align="center", text_baseline="middle")

                # p.segment(x0=arqi["groupt"], y0=arqi["period"], x1=arqi["groupt"], y1=arqi["period"], line_color="#f4a582", line_width=1)
                from bokeh.models import CustomJS
                # code_hover = '''
                # if (cb_data.index.indices.length > 0) {
                #     var active_index = cb_data.index.indices[0]
                #     var data = cb_data.renderer.data_source.data
                #     var show_tooltip = data['active'][active_index]
                #     var tooltip_index = 0
                #     cb_data.index.indices.width=50px
                #
                #
                # }
                # '''

                # p.xaxis.bounds = (0, 10)
                p.outline_line_color = None
                p.grid.grid_line_color = None
                p.axis.axis_line_color = None
                p.axis.major_tick_line_color = None
                # p.axis.major_label_standoff = 1

                # p.legend.orientation = "horizontal"
                # p.legend.location ="top_center"
                p.hover.renderers = [r]  # only hover element boxes
                # p.hover.callback = CustomJS(code=code_hover)

                # output_file('filename.html')
                #show(p)
                from bokeh.embed import components

                #st.components.v1.iframe(p, height=600, width=1700, scrolling=True)
                #html = file_html(p, CDN, "my plot")
                #st.bokeh_chart(html, use_container_width=True)
                
               # script, div = components(p)
               #  html = template.render(resources=resources,
               #                         script=script,
               #                         div=div)

                #HtmlFile = open("SBMEtab.html", 'r', encoding='utf-8')
                
                handle = file_html(p, CDN, "my plot")

                #source_code = HtmlFile.read()
                source_code =handle

               # print(source_code)
               # ppp=components.html(source_code)
                #ppp = open("SBMEtab.html")
                #components.html(ppp.read())
               # PP=_data_url_to_image(p)

                # save(p)




            
            except:# Exception as err:
                continue
                #print(f"Unexpected {err=}, {type(err)=}")
            return source_code

  # tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 \
    #                 , tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23, tab24 \
    #                 ,tab25, tab26, tab27, tab28 = st.tabs(
    #     ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBFS', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
    #      'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN', 'SBPL',
    #      'SBPJ'])
pt1 = pd.read_csv('/mount/src/edomenico/metar_trat_teste1.csv',
                                    sep=',',
                                    decimal='.')
pt2 = pd.read_csv('/mount/src/edomenico/metar_trat_teste2.csv',
                                    sep=',',
                                    decimal='.')
    
    
atudados_area1=0
atudados_area2=0
area = ['Área 1', 'Área 2']
area_1 = ['SBJR','SBES', 'SBME', 'SBFS', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
              'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG','SNRU', 'SBFN', 'SBPL',
              'SBPJ']
area_2 = ['SBRD', 'SBVH', 'SBJI','SSKW','SBRB', 'SWEI', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA', 'SBCJ', 'SBHT',
              'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SWPI', 'SBMY', 'SBTF','SBUY', 'SBUA', 'SBEG',
              'SBBV']
start_date = datetime.today()
end_date = datetime.today()
start_datee = datetime.today()
with st.sidebar:
        st.write('Gerenciamento dos dados')
with st.container(border=True):
            on = st.toggle('Atualizar os dados (Áreas 1 e 2)')

            
           # selori = st.radio("Escolha a origem",["Redemet", "AWC"],horizontal=True)
            
if on: 
                selori = st.radio("Escolha a origem",["Redemet", "AWC"],horizontal=True)
if selori=="Redemet":
                    
               
                        too_data = format(datetime.utcnow(), "%d/%m/%Y")
                        to_data = st.date_input('Inicio:', start_date)
                        from_data = st.date_input('Fim:', end_date)
                        if st.button('Atualizar'):
                            progress_text = "Processando... Aguarde."
                            my_bar = st.progress(0, text=progress_text)
                            pt = rest(1,to_data,from_data,'REDEMET')
                            my_bar.progress(50, text="Em andamento...")
                                # for percent_complete in range(100):
                                #     time.sleep(0.01)
                            pt = rest(2,to_data,from_data,'REDEMET')
                
                            my_bar.progress(100, text="Terminou")
else:
                if st.button('Atualizar'):
                        too_data = format(datetime.utcnow(), "%d/%m/%Y")
                        to_data = too_data
                        from_data = too_data
                        progress_text = "Processando... Aguarde."
                        my_bar = st.progress(0, text=progress_text)
                        pt1 = rest(1,to_data,from_data,'AWC')
                        my_bar.progress(50, text="Em andamento...")
                        pt1 = rest(2,to_data,from_data,'AWC')
            
                        my_bar.progress(100, text="Terminou")
            
                    
                #if atualizardados=='Último dia':
        
        
                #if st.button('Consultar'):
                    
            #st.divider()
            #on3 = st.toggle('Atualizar pelo AWC - 72h anteriores')
            #if on3:
            #    too_data = format(datetime.utcnow(), "%d/%m/%Y")
            #    to_data = too_data
            #    from_data = too_data
            #    if st.button('Atualizar_AWC'):
            #        progress_text = "Processando... Aguarde."
            #        my_bar = st.progress(0, text=progress_text)
             #       pt1 = rest(1,to_data,from_data,'AWC')
             #       my_bar.progress(50, text="Em andamento...")
            #        pt1 = rest(2,to_data,from_data,'AWC')
        
            #        my_bar.progress(100, text="Terminou")
                    
st.divider()
on2 = st.toggle('Consultar outro período')
            
if on2:
                selecionaperiodo= st.radio('Escolha o período',['Últimos 10 dias','Selecionar dia inicial (a partir de 01/05/25)'],horizontal=True)
                if selecionaperiodo=='Últimos 10 dias':
                    datainicial = datetime.utcnow() - timedelta(9)
                else:
                    too_data = st.date_input('Dia Inicial:', start_datee)
                    datainicial=too_data
                   # datainicial= datainicial-timedelta(9)
else:
                datainicial = datetime.utcnow() - timedelta(9)
                ong=st.toggle('Mostrar gráfico')
        
        
        #st.divider()
st.write('Visualização dos dados')
with st.container(border=True):
           # st.divider()
            
            
            
            
            selarea = st.radio("Escolha a área",["Área 1", "Área 2"],horizontal=True)
            st.divider()
    
            #col1, col2 = st.columns(2)
        if selarea=="Área 1":
                #with col1:
                    #st.header('Área 1')
                nomedaestacao= st.radio(
                        "Área 1",
                        area_1)
                noarea=1
    
        else:
               # st.header('Área 2')
                nomedaestacao=  st.radio(
                    "Área 2",
                    area_2)
                noarea = 2
st.markdown(
            """
            
            e-mail: edomenico813@gmail.com

           
            """
        )
if ong:
        print('antes de entrar')
        print(datainicial)
        df = obterarq(nomedaestacao, noarea, datainicial)
with st.container():
            df['dryt'] = pd.to_numeric(df['dryt'], downcast='signed')
            df['dewp'] = pd.to_numeric(df['dewp'], downcast='signed')
            df['pres'] = pd.to_numeric(df['pres'], downcast='signed')
            #df['vis'] = pd.to_numeric(df['vis'], downcast='signed')
            df['wspd'] = pd.to_numeric(df['wspd'], downcast='signed')
            df['wdir'] = pd.to_numeric(df['wdir'], downcast='signed')
           # df['gust'] = pd.to_numeric(df['gust'], downcast='signed')
            df['pres'] = pd.to_numeric(df['pres'], downcast='signed')
            df['altn1'] = pd.to_numeric(df['altn1'], downcast='signed')
            df['altn2'] = pd.to_numeric(df['altn2'], downcast='signed')
            df['altn3'] = pd.to_numeric(df['altn3'], downcast='signed')
            df['altn4'] = pd.to_numeric(df['altn4'], downcast='signed')
            #df['altncb'] = pd.to_numeric(df['altncb'], downcast='signed')

            st.header(df['estacao'].iloc[-1])
            #st.subheader(str(df['datahora'].iloc[0][0:16]) + 'UTC')
            st.subheader(str(df['data_hora'].iloc[-1])[0:16] + 'UTC')
            col1, col2, col3 = st.columns(3)
            with col1:
                #col1.metric("Temperatura(°C)", f"{(int(df['dryt'].iloc[-1]))}")
                col1.metric("Temperatura(°C)", f"{(df['dryt'].iloc[-1])}")
                if df['qn1'].iloc[-1] == 'FEW':
                    sceu = 'Poucas nuvens'
                elif df['qn1'].iloc[-1] == 'SCT':
                    sceu = 'Parcialmente nublado'
                elif df['qn1'].iloc[-1] == 'BKN':
                    sceu = 'Nublado'
                elif df['qn1'].iloc[-1] == 'OVC':
                    sceu = 'Encoberto'
                else:
                    sceu = 'Claro'

                # col1.metric("Céu", f"{df['ceu'].iloc[0]}")
                col1.metric("Céu", sceu)
                col1.metric("Umidade(%)", f"{df['ur'].iloc[-1]}")

                with col2:
                        if df['tp'].iloc[-1] == 'BR':
                            stp = 'Névoa úmida'
                        elif df['tp'].iloc[-1] == 'RA':
                            stp = 'Chuva moderada'
                        elif df['tp'].iloc[-1] == 'TS':
                            stp = 'Trovoada'
                        elif df['tp'].iloc[-1] == 'TSRA':
                            stp = 'Trovoada com chuva'
                        elif df['tp'].iloc[-1] == '+TSRA':
                            stp = 'Trovoada com chuva forte'
                        elif df['tp'].iloc[-1] == '-TSRA':
                            stp = 'Trovoada com chuva leve'
                        elif df['tp'].iloc[-1] == '+RA':
                            stp = 'Chuva forte'
                        elif df['tp'].iloc[-1] == '-RA':
                            stp = 'Chuva leve'
                        elif df['tp'].iloc[-1] == 'HZ':
                            stp = 'Névoa seca'
                        elif df['tp'].iloc[-1] == 'FU':
                            stp = 'Fumaça'
                        elif df['tp'].iloc[-1] == 'DZ':
                            stp = 'Chuvisco moderado'
                        elif df['tp'].iloc[-1] == '-DZ':
                            stp = 'Chuvisco leve'
                        elif df['tp'].iloc[-1] == '+DZ':
                            stp = 'Chuvisco forte'
                        elif df['tp'].iloc[-1] == 'SHRA':
                            stp = 'Pancada de chuva moderada'
                        elif df['tp'].iloc[-1] == '-SHRA':
                            stp = 'Pancada de chuva leve'
                        elif df['tp'].iloc[-1] == '+SHRA':
                            stp = 'Pancada de chuva forte'
                        elif df['tp'].iloc[-1] == 'VCSH':
                            stp = 'Pancada de chuva na vizinhança'
                        elif df['tp'].iloc[-1] == 'VCTS':
                            stp = 'Trovoada na vizinhança'
                        elif df['tp'].iloc[-1] == 'FG':
                            stp = 'Nevoeiro'
                        elif df['tp'].iloc[-1] == 'BCFG':
                            stp = 'Banco de nevoeiro'
                        else:
                            stp = 'Nil'
                # col2.metric("Tempo presente", f"{(df['tp'].iloc[0])}")
                col2.metric("Tempo presente", stp)
                col2.metric("Visibilidade(m)", f"{(df['vis'].iloc[-1])}")
                col2.metric("Pressão(hPa)", f"{(df['pres'].iloc[-1])}")
        with col3:
                # col3.metric("Tempo", f"{df['tp'].iloc[0]}")
                #col3.metric("Rajada(kt)", f"{(df['gust'].iloc[-1])}")
                col3.metric("Vento(graus/kt)", f"{(df['wdir'].iloc[-1])} / {(df['wspd'].iloc[-1])}")
                
                col3.metric("Altura nuvens baixas(x100ft)", f"{(df['altn1'].iloc[-1])}")

            st.divider()

        with st.container():


                col1, col2= st.columns((5, 5))
                with col1:
                    min_max2(df)
                with col2:
                    vento2(df)
                col3, col4 = st.columns((5, 5))
                with col3:
                    temp_time_series2(df)
                with col4:
                    weather_pie(df)
            st.divider()

        with st.expander(label="Mostrar dados:"):
                df1=df

                # df1['dryt']=pd.to_numeric(df1['dryt'], downcast='signed')
                # df1['dewp'] = pd.to_numeric(df1['dewp'], downcast='signed')
                # df1['pres'] = pd.to_numeric(df1['pres'], downcast='signed')
                # df1['vis'] = pd.to_numeric(df1['vis'], downcast='signed')
                # df1['wspd'] = pd.to_numeric(df1['wspd'], downcast='signed')
                #df1['wdir'] = pd.to_numeric(df1['wdir'], downcast='signed')
                # df1['gust'] = pd.to_numeric(df1['gust'], downcast='signed')
                # df1['pres'] = pd.to_numeric(df1['pres'], downcast='signed')
                # df1['altn1'] = pd.to_numeric(df1['altn1'], downcast='signed')
                # df1['altn2'] = pd.to_numeric(df1['altn2'], downcast='signed')
                # df1['altn3'] = pd.to_numeric(df1['altn3'], downcast='signed')
                # df1['altn4'] = pd.to_numeric(df1['altn4'], downcast='signed')
                # df1['altncb'] = pd.to_numeric(df1['altncb'], downcast='signed')
                df1.drop('data_hora', inplace=True, axis=1)
                df1.drop('drytt', inplace=True, axis=1)
                df1.drop('dewpt', inplace=True, axis=1)
                df1.drop('metar', inplace=True, axis=1)
                df1.drop('speci', inplace=True, axis=1)
                df1.drop('data', inplace=True, axis=1)
                df1.drop('data1', inplace=True, axis=1)
                st.table(df1)
    
    
    p=tabuleiro(nomedaestacao,noarea,datainicial)
        
    import streamlit.components.v1 as components
    #from streamlit_bokeh import streamlit_bokeh
    
    #streamlit_bokeh(p)
    st.components.v1.html(p,  height=2400,width=1700, scrolling=True)
    #st.components.v1.html(p)
    #st.bokeh_chart(p)
    #st.bokeh_chart(p, use_container_width=True)
    
    
            # from streamlit_bokeh_events import streamlit_bokeh_events
            # event_result = streamlit_bokeh_events(
            #     events="TestSelectEvent",
            #     bokeh_plot=p,
            #     key="foo",
            #     debounce_time=1000,
            # )
            # st.subheader("Raw Event Data")
            # st.write(event_result)
        #st.bokeh_chart(html_content,use_container_width=True)
            #st.write(p)
        #if st.button('Atualizar dados'):
        #    if noarea==1:
         #       pt1 = rest(noarea)
         #       atudados_area1=1
            
          #      pt2 = rest(2)
           #     atudados_area2=2
                
        #barra_lateral = st.sid,ebar.empty()
       # area_seleciona = st.sidebar.selectbox("Seleciona a área:", area)
    #if __name__ == '__main__':
        
        #if streamlit._is_running_with_streamlit:
     #   main()
        #else:
        #    sys.argv = ["streamlit", "run", sys.argv[0]]
        #    #app.run_server(debug=True, port=8881)
          #  sys.exit(stcli.main())    
st.set_page_config(
        page_title="Tabuleiro - CMA-GL",
        page_icon="✅",
        layout="wide",
    )
#st.session_state

