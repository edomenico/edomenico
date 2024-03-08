import time  # to simulate a real time data, time loop
import rosadosventos
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import sys
#from streamlit.web import cli as stcli
# Set up the Chrome driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # to simulate a real time data, time loop
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
import numpy as np
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
def main2():
    def rest(areas, to_data, from_data,nome_estacao):
        import time  # to simulate a real time data, time loop

        import numpy as np  # np mean, np random
        import pandas as pd  # read csv, df manipulation
        import plotly.express as px  # interactive charts
        import sys
        # from streamlit.web import cli as stcli

        import streamlit
        from streamlit import runtime
        from streamlit_toggle import toggle
        from streamlit.web import cli as stcli
        import streamlit as st
        from datetime import datetime, timedelta
        import os
        import glob
        global pt

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
                global df, arqi
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
            estado = areasele
            areatrab = areasele

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
            metar = []
            speci = []

            for i in range(len(arqi)):

                if arqi.Mensagem[
                    i] == 'METAR SBJR 171300Z 22002KT 9000 4000SW SCT010 SCT025 BKN040 24/21 Q1018=':
                    c = 6

                if arqi.Mensagem[i].find('COR') > -1:
                    novamens = 'METAR ' + arqi.Mensagem[i][
                                          arqi.Mensagem[i].find('COR') + 4:len(arqi.Mensagem[i])]

                    mensagem1 = novamens.split()
                    mens = novamens

                else:

                    mensagem1 = arqi.Mensagem[i].split()
                    mens = arqi.Mensagem[i]

                # print(len(mensagem1))

                if mensagem1[0] == 'METAR' or mensagem1[0] == 'SPECI':
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
                        if j == 2:
                            # data_hora=mensagem1[j][2:4]+':'+mensagem1[j][4:6]
                            data_hora = mensagem1[j][2:4] + ':00'  # + mensagem1[j][4:6]
                            if estacao[k] == 'SBFN' and data_hora == "20:00":
                                GGGGGGGGG = 1

                        # campo 3 vento
                        # arqi.Mensagem[i][arqi.Mensagem[i].find('KT')
                        if mensagem1[j].find('SB') > -1 or mensagem1[j].find('SSKW') > -1 or mensagem1[j].find(
                                'SWPI') > -1 or mensagem1[j].find('SWEI') > -1:
                            estacao.append(mensagem1[j])
                        # if estacao[k] == 'SBFZ':
                        #      GGGGGGGGG = 1

                        # if k==190:
                        # print('k= ',k,estacao[k])
                        # print('data',datahora[k-1])

                        if mensagem1[j].find('KT') > -1:
                            if len(wdir) == len(dryt):
                                if (mensagem1[j][0:3]) == 'VRB' or (mensagem1[j][0:3]) == '///':

                                    wdir.append('NaN')
                                else:
                                    if mensagem1[j][0:3] == "OOO":
                                        wdir.append(0)
                                    else:
                                        try:
                                            wdir.append(float(mensagem1[j][0:3]))
                                        except ValueError:
                                            wdir.append('NaN')

                                if (mensagem1[j][3:5]) == '//' or mensagem1[j].find('P') > -1:
                                    wspd.append('NaN')
                                else:
                                    if mensagem1[j][3:5] == 'OO':
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

                        if mensagem1[j].find('CAVOK') > -1 and aviso == False and entrou == False:
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
                                'V') == -1 and mensagem1[j].find('F') == -1 and mensagem1[j].find('S') == -1 and \
                                mensagem1[j].find('B') == -1 and mensagem1[j].find(
                            'O') == -1 and entrou == False:
                            vis.append(mensagem1[j])
                            entrou = True
                            print('j4 1', mensagem1[j])

                        # vento variavel nao cavok
                        if j == 5 and mensagem1[j - 1].find('V') > -1 and mensagem1[j].find('CAVOK') == -1 and \
                                mensagem1[
                                    j - 1].find('CAVOK') == -1 and mensagem1[j].find(
                            'R') == -1 and entrou == False:
                            vis.append(mensagem1[j])
                            entrou = True
                            print('j5 1', mensagem1[j])

                        # automatica
                        if j == 5 and aviso == True and entrou == False and (
                                mensagem1[j].find('V') == -1 or mensagem1[j].find('CAVOK') > -1):
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
                                print('j5 2', mensagem1[j])
                            entrou = True

                        if (mensagem1[j] == ('////') and entrou == False):
                            vis.append('NaN')
                            entrou = True

                        if j == 6 and aviso == True and entrou == False and mensagem1[j].find('/') == -1:
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

                        if mensagem1[j].find('Q') > -1 and mensagem1[j].find(
                                'S') != 0:  # and bool(re.search(r'\d', mensagem1[j])):
                            if (mensagem1[j][1:5]) == '////':
                                pres.append('NaN')
                            else:

                                try:
                                    # print(mensagem1[j])

                                    pres.append(float(mensagem1[j][1:5]))


                                except ValueError:
                                    pres.append('NaN')
                                    if len(pres) != len(dryt):
                                        dryt.append('NaN')
                                    if len(pres) != len(dewp):
                                        dewp.append('NaN')

                            break

                        # if tempentrou== False:
                        #  if mensagem1[j].find('/') > -1 and bool(re.search(r'\d', mensagem1[j])) and mensagem1[j + 1].find(
                        #              'Q') > -1:
                        # print(mensagem1[j])
                        if mensagem1[j].find('/') > -1 and mensagem1[j + 1].find('Q') > -1:

                            # print(mensagem1[j][0:2])
                            # print(mensagem1[j][3:5])
                            #  print(mensagem1[j + 1])
                            if (mensagem1[j][0:2]) == '//':

                                dryt.append('NaN')
                            else:
                                dryt.append(float(mensagem1[j][0:2]))
                            if (mensagem1[j][3:5]) == '//':
                                dewp.append('NaN')
                            else:
                                if mensagem1[j][3:5].find('M') > -1:
                                    dewp.append(float(mensagem1[j][4:6]) * -1)
                                else:

                                    dewp.append(float(mensagem1[j][3:5]))
                                    # tempentrou = True

                        if mensagem1[j].find('FEW') > -1 or mensagem1[j].find('SCT') > -1 or mensagem1[j].find(
                                'BKN') > -1 or \
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
                        if mensagem1[j].find('CB') > -1 and len(mensagem1[j]) > 4 and nuvemcb == False:
                            altncb.append(((mensagem1[j][3:6])))
                            qncb.append((mensagem1[j][0:3]))
                            nuvemcb = True
                        if mensagem1[j].find('TCU') > -1 and len(mensagem1[j]) > 4 and nuvemcb == False:
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

                        if (mensagem1[j].find('RA') > -1 or mensagem1[j].find('DZ') > -1 or mensagem1[j].find(
                                'BR') > -1 or
                            mensagem1[j].find('HZ') > -1 or mensagem1[j].find('FG') > -1 or mensagem1[j].find(
                                    'FU') > -1 or mensagem1[j].find('VC') > -1 or
                            mensagem1[j].find('TS') > -1) and mensagem1[j].find('SB') == -1 and mensagem1[
                            j].find(
                            'OVC') == -1 and tempopres == False:
                            tp.append((mensagem1[j][0:len(mensagem1[j])]))
                            tempopres = True

                    datahora.append(arqi['Data'][i] + ' ' + data_hora)
                    try:
                        xhor = datetime.strptime(datahora[k], '%d/%m/%Y %H:%M')
                    except ValueError:
                        if k > 0:
                            datahora[k] = datahora[k - 1]
                    else:
                        datahora[k] = xhor
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
                        print(estacao[k], datahora[k])
                    if mensagem1[0] == 'SPECI':
                        speci.append(mens)
                        print('aqui', datahora[k])
                        print(mens)
                        metar.append('-')
                    else:
                        metar.append(mens)
                        speci.append('-')
                    if estacao[k] == 'SWPI':
                        yyyyyyyyy = 1
                    if vis[k] == '////':
                        vis[k] = '-9999'
                    if len(wspd) != len(pres):
                        pres.append('NaN')
                        if len(pres) != len(dryt):
                            dryt.append('NaN')
                            dewp.append('NaN')
                    df.loc[k] = [estacao[k]] + [datahora[k]] + [wspd[k]] + [wdir[k]] + [gust[k]] + [dryt[k]] + [
                        dewp[k]] + [pres[k]] + [vis[k]] + [tp[k]] + [
                                    altn1[k]] + [qn1[k]] + [altn2[k]] + [qn2[k]] + [altn3[k]] + [qn3[k]] + [
                                    altn4[k]] + [qn4[k]] + [
                                    altncb[k]] + [qncb[k]] + [metar[k]] + [speci[k]]
                    # f.sort_values(by=['First Column', 'Second Column', ...], inplace=True)

                    df.sort_values(by=['estacao', 'datahora'], inplace=True)

                    df.to_csv('metar_trat_' + str(estado) + '.csv', encoding='utf-8', index=False,
                              date_format='%d/%m/%Y %H:%M')

            # -----------------------juntar arquivos
            arqiago = pd.read_csv('metar_trat_' + str(estado) + '.csv',
                                  sep=',',
                                  decimal='.')
            # x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in arqiago.datahora]
            # arqiago['data_hora'] = x
            if areatrab == 1:
                arqiant = pd.read_csv('/mount/src/edomenico/metar_trat_teste1.csv',
                                      sep=',',
                                      decimal='.')
            else:
                arqiant = pd.read_csv('/mount/src/edomenico/metar_trat_teste2.csv',
                                      sep=',',
                                      decimal='.')

            df1 = pd.concat([arqiant, arqiago])
            df1.sort_values(by=['datahora', 'estacao'], inplace=True)
            df1 = df1.drop_duplicates(['estacao', 'datahora', 'speci'])

            if areatrab == 1:
                df1.to_csv('metar_trat_teste1.csv', encoding='utf-8', index=False, date_format='%d/%m/%Y %H:%M')
            else:
                df1.to_csv('metar_trat_teste2.csv', encoding='utf-8', index=False, date_format='%d/%m/%Y %H:%M')

            return df1

        # --------------------------------------------------------

        start_date = datetime.today()

        end_date = datetime.today()

        area = ['Área 1', 'Área 2']
        area_1 = ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS',
                  'SBAC',
                  'SBJE',
                  'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG',
                  'SBFN',
                  'SBPL',
                  'SBPJ']
        area_2 = ['SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA',
                  'SBCJ',
                  'SBHT',
                  'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBMY', 'SBTF',
                  'SBUA',
                  'SBEG',
                  'SBBV',
                  'SSKW', 'SWEI', 'SWPI']
        # st.set_page_config(
        #         page_title="Dados Estatísticos",
        #         page_icon="✅",
        #         layout="wide",
        #     )
        # barra_lateral = st.sidebar.empty()
        # area_seleciona = st.sidebar.selectbox("Seleciona a área:", area)
        # if area_seleciona == 'Área 1':
        #     areaprev=1
        #     areasel = area_1
        #     estacao = 'SBJR,SBAC,SBAR,SBCB,SBCP,SBES,SBFS,SBFN,SBFZ,SBGL,SBJE,SBJP,SBJU,SBKG,SBME,SBMO,SBMS,SBNT,SBPB,SBPJ,SBPL,SBPS,SBRF,SBRJ,SBSL,SBSG,SBTE,SBVT,'
        # else:
        ##    areasel = area_2
        #    estacao = 'SBRD,SBVH,SWEI,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SWPI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SBTF,SBUA,SBEG,SBBV,'
        # to_data = st.sidebar.date_input('Inicio:', start_date)
        # from_data = st.sidebar.date_input('Fim:', end_date)
        datainicio = datetime.utcnow()
        if nome_estacao =='N':
            if areas == 1:
                areasel = area_1
                areaprev = 1
                estacao = 'SBJR,SBAC,SBAR,SBCB,SBCP,SBES,SBFS,SBFN,SBFZ,SBGL,SBJE,SBJP,SBJU,SBKG,SBME,SBMO,SBMS,SBNT,SBPB,SBPJ,SBPL,SBPS,SBRF,SBRJ,SBSL,SBSG,SBTE,SBVT,'
            else:
                areasel = area_2
                areaprev = 2
                estacao = 'SBRD,SBVH,SWEI,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SWPI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SBTF,SBUA,SBEG,SBBV,'
        else:
            estacao=nome_estacao
            areasel = area_2
            areaprev = 2
        pdf = redemet_baixa(1, areasel, to_data, from_data, estacao)

        pdff = trata_redemet(areaprev)
        edited_df = st.data_editor(pdff)
        return pdff

    def _data_url_to_image(data_url: str) -> Image:
        """Convert DataURL string to the image."""
        _, _data_url = data_url.split(";base64,")
        return Image.open(io.BytesIO(base64.b64decode(_data_url)))

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
                #datahi = datetime.strftime(datahini, '%d/%m/%Y')
                #datahf = datetime.strftime(datahfim, '%d/%m/%Y')
               # tempo = datahfim - datahini
    
                if datahini == datahfim:
                    intervalo = 0
                else:
                    intervalo = (datahfim - datahini).days
                #mes = datahini.month
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
                    if i != 0:
                        datacoris = datahini + timedelta(days=i)
                        datacoris = datacoris + timedelta(minutes=0)
                        datacorfs = datacoris + timedelta(hours=23)
                        # datacori=datahf
                    else:
                        # datacori = datahini + timedelta(days=i)
                        datacoris = datahini + timedelta(minutes=0)
                        datacorfs = datahini + timedelta(hours=23)

                    datacoris = datetime.strftime(datacoris, '%d/%m/%Y %H:%M')
                    # #datacori = datetime.strftime(datacori, '%d/%m/%Y %H:%M')
                    # datacorf=  datacori + timedelta(hours=23)
                    datacorfs = datetime.strftime(datacorfs, '%d/%m/%Y %H:%M')
                    datacorfs = datacorfs[0:10] + ' 23:00'
    
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
                    #browser.quit()
                print(df)
                # df = df.drop(columns=['Unnamed: 0'])
                os.chdir("/mount/src/edomenico/area1")
                df.to_csv("metar.csv", header=True)
                # df.to_csv('example.csv')
                return df






    def tabuleiro(est, areatrab, datainicio,pt1,pt2):
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
                    if (date.today().year % 4) != 0:
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
                                            var mapping = {1: 22, 2: 23, 3: 24, 4: 25, 5:26, 6: 27, 7: 28, 8: 29, 9: 30, 10: 1};
                                            return mapping[tick];
                                       """)
                    else:
                        p.xaxis.formatter = FuncTickFormatter(code="""
                                                                    var mapping = {1: 22, 2: 23, 3: 24, 4: 25, 5:26, 6: 27, 7: 28, 8: 29, 9: 1, 10: 2};
                                                                    return mapping[tick];
                                                               """)

                elif mesini == 1 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
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
                                               var mapping = {1: 28, 2: 1, 2: 2, 3: 3, 4:4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9};
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

        # pd.set_option('max_columns', None)
        # areatrab = 1  # dado entrada
        # datainicio='27/03/20'#dado entrada

        # datainicio = datetime.utcnow() - timedelta(9)
        datainicio = datainicio.strftime('%d/%m/%y')

        if areatrab == 1:
            #  estacao_area = 'SBJR,SBES,SBME,SBCP,SBFS,SBRJ,SBCB,SBVT,SBPS,SBGL,SBNT,SBMS,SBAC,SBJE,SBPB,SBAR,SBMO,SBRF,SBJP,SBSG,SBFZ,SBSL,SBTE,SBJU,SBKG,SBFN,SBPL,SBPJ'
            # estacao_area = 'SBFZ,'
            arqi1 = pd.read_csv('metar_trat_teste1.csv')
        else:

            # estacao_area = 'SBRD,SBVH,SWEI,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SWPI,SBTF,SBUA,SBEG,SBBV'  # sem SBMY SBCY
            # estacao_area = 'SBVH'
            # estacao_area ='SBEG,'
            arqi1 = pd.read_csv('metar_trat_teste2.csv')
        estacao_area = est
        noestacao = estacao_area.split(',')

        for i in range(0, 1, 1):
            try:
                nome_estacao = noestacao[i]
                arqi = arqi1.loc[(arqi1['estacao'] == nome_estacao)]
                arqi = arqi.reset_index(drop=True)
                # cwd = os.getcwd()
                # if areatrab == 1:
                #
                #     if os.path.isdir(cwd + '/tabuleiro/area1/'):
                #         caminho = cwd + '/tabuleiro/area1/'
                #     else:
                #         mkdir(cwd + '/tabuleiro/area1/')
                #         caminho = cwd + '/tabuleiro/area1/'
                # else:
                #     if os.path.isdir(cwd + '/tabuleiro/area2/'):
                #         caminho = cwd + '/tabuleiro/area2/'
                #     else:
                #         mkdir(cwd + "/tabuleiro/area2/")
                #         caminho = cwd + '/tabuleiro/area2/'
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
                                if (jj - iii) < 0:
                                    break
                            # noespec[jj-iii] = str(iii+2)
                        #
                        #
                        else:
                            noespec[jj] = '1'

                        #         especi.append('-')
                # arqi['especial'] = arqi['especi'].str[:10]

                # arqi['especial']=especi
                arqi['valor'] = valores
                arqi['aviso'] = stop
                arqi['nspc'] = noespec
                print(valores)
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
                    if date_fim.month == 3:
                        if date_fim.year % 4 == 0:
                            dia_fim = '29'
                            mes_fim = str(date_fim.month - 1)
                            ano_fim = str(date_fim.year)
                        else:
                            dia_fim = '28'
                            mes_fim = str(date_fim.month - 1)
                            ano_fim = str(date_fim.year)
                else:
                    dia_fim = str(date_fim.day - 1)
                    ano_fim = str(date_fim.year)

                datatit = dia_ini + '/' + mes_ini + '/' + ano_ini + ' a ' + dia_fim + '/' + mes_fim + '/' + ano_fim
                arqi = arqi.loc[(arqi['data_hora'] >= date_inicio)]
                arqi = arqi.loc[(arqi['data_hora'] < date_fim)]
                arqi.sort_values(by=['estacao', 'data_hora'], inplace=True)
                arqi = arqi.reset_index(drop=True)
                # print('arq: ', arqi)
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

                            dia.append(29 - deltatempo + 1)
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
                periods = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                           "16", "17",
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
                vmax = []
                vmin = []
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
                            vmax.append(ccmax.wspd[bbb])
                            vmin.append(ccmin.wspd[bbb])

                arqi['tmax'] = tmax
                arqi['tmin'] = tmin
                arqi['vmax'] = vmax
                arqi['vmin'] = vmin

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
                        uuu = round(100 - 5 * (at - atb))
                        ur.append(uuu)
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
                arqi['tp'] = arqi['tp'].replace(['-DZ'], "-" + d)
                arqi['tp'] = arqi['tp'].replace(['+DZ'], "+" + d)
                arqi['tp'] = arqi['tp'].replace(['FU'], g)
                arqi['tp'] = arqi['tp'].replace(['VCFG'], e)
                arqi['tp'] = arqi['tp'].replace(['FG'], e)
                arqi['tp'] = arqi['tp'].replace(['BCFG'], e)
                arqi['tp'] = arqi['tp'].replace(['FZFG'], e)
                arqi['tp'] = arqi['tp'].replace(['BR'], h)
                arqi['tp'] = arqi['tp'].replace(['HZ'], k)
                arqi['tp'] = arqi['tp'].replace(['VCSH'], ').(')
                arqi['tp'] = arqi['tp'].replace(['-SHRA'], "-" + m)
                arqi['tp'] = arqi['tp'].replace(['+SHRA'], "+" + m)
                arqi['tp'] = arqi['tp'].replace(['SHRA'], m)
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
                        if ("VRB" in str(arqi.metar[iwdir])):
                            wdirwdir.append('VRB')
                        else:
                            wdirwdir.append('0' + auxwdir[0:1])
                    else:
                        wdirwdir.append(auxwdir[0:2])
                arqi["wdirstr"] = wdirwdir
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
                    if int(arqi['vis'][inuv]) == 99 and arqi['qn1'][inuv] == "" and arqi['tp'][inuv] == "" and \
                            arqi['qncb'][
                                inuv] == "":
                        auxvis[inuv] = 'CVK'
                    if int(arqi['vis'][inuv]) != 99 and arqi['qn1'][inuv] == "":
                        auxqn1[inuv] = 'NSC'
                        # arqi['qn1'][inuv].mask(arqi['qn1'][inuv] == "", 'NSC', inplace=True)
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
                &nbsp&nbsp&nbsp&nbsp Tmáx: @tmax°C&nbsp&nbsp Tmin: @tmin°C&nbsp&nbsp Vmax: @vmax kt&nbsp&nbsp Vmin: @vmin kt</b>
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
                p.yaxis.axis_label = 'H O R A'
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
                r = p.rect("group", "period", width=1.0, height=1, source=arqi,
                           fill_alpha=0.6)  # , legend_field="dryt")
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

                # p.circle([1,
                # 2, 3, 4, 5,6, 7, 8, 9, 10], [1, 2, 3, 4, 5,6, 7, 8, 9, 10], size=10, color="navy", alpha=0.5)
                p.text(x=x, y=dodge("period", 0.3, range=p.y_range), text="dryt", text_font_style="bold",
                       text_font_size="11px", **text_props)

                p.text(x=dodge("group", -0.07, range=p.x_range), y=dodge("period", 0.3, range=p.y_range),
                       text="aviso",
                       text_font_style="bold",
                       text_font_size="11px", **text_props)

                # print(x)

                p.text(x=x, y=dodge("period", -0.35, range=p.y_range), text="de", text_font_style="bold",
                       text_font_size="11px", **text_props)
                p.text(x=x, y=dodge("period", -0.05, range=p.y_range), text="vis", text_font_style="bold",
                       text_font_size="11px", **text_props)
                p.text(x=dodge("group", -0.3, range=p.x_range), y=dodge("period", 0.05, range=p.y_range),
                       text="tp",
                       text_font_style="bold",
                       text_font_size="18px", text_color='red', **text_props)
                p.text(x=dodge("group", 0.3, range=p.x_range), y=dodge("period", 0.3, range=p.y_range),
                       text="pres",
                       text_font_style="bold",
                       text_font_size="11px", **text_props)

                p.text(x=dodge("group", -0.07, range=p.x_range), y=dodge("period", -0.4, range=p.y_range),
                       text="qn1",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)
                p.text(x=dodge("group", 0.065, range=p.x_range), y=dodge("period", -0.4, range=p.y_range),
                       text="altn1",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)

                p.text(x=dodge("group", -0.07, range=p.x_range), y=dodge("period", -0.2, range=p.y_range),
                       text="qn2",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)
                p.text(x=dodge("group", 0.065, range=p.x_range), y=dodge("period", -0.2, range=p.y_range),
                       text="altn2",
                       text_font_style="bold",
                       text_font_size="9px", **text_props)

                p.text(x=dodge("group", 0.07, range=p.x_range), y=dodge("period", -0.3, range=p.y_range),
                       text="qncb",
                       text_font_style="bold", text_color='red',
                       text_font_size="9px", **text_props)
                p.text(x=dodge("group", 0.20, range=p.x_range), y=dodge("period", -0.3, range=p.y_range),
                       text="altncb",
                       text_font_style="bold", text_color='red',
                       text_font_size="9px", **text_props)

                p.text(x=dodge("group", 0.06, range=p.x_range), y=dodge("period", -0.05, range=p.y_range),
                       text="gust",
                       text_font_style="bold", text_color='red',
                       text_font_size="9px", **text_props)

                # -----dia 19
                p.text(x=dodge("group", 0.06, range=p.x_range), y=dodge("period", 0.1, range=p.y_range),
                       text="wdirstr",
                       text_font_style="bold", text_color='black',
                       text_font_size="9px", **text_props)
                #### Intensidade do vento
                p.text(x=dodge("group", 0.4, range=p.x_range), y=dodge("period", -0.35, range=p.y_range),
                       text="wspd",
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

                yyy = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5,
                       16.5, 17.5,
                       18.5, 19.5, 20.5, 21.5, 22.5, 23.5]
                yyyyyy = [0.8, 1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8, 9.8, 10.8, 11.8, 12.8, 13.8, 14.8, 15.8,
                          16.8, 17.8,
                          18.8, 19.8, 20.8, 21.8, 22.8, 23.8]
                xxx = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
                xxxxxx = [1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1,
                          1.1, 1.1,
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

                                        xxxxxx.append(
                                            (xxxxx[aux] + 0 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
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

                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.10 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.10 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
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
                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
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
                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append(
                                            (xxxxx[aux] + 0.1 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y9.append(
                                            (yyyyy[aux] + 0.1 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 120))))
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
                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append((xxxxx[aux] + 0.20 * np.sin(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append((yyyyy[aux] + 0.20 * np.cos(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 105))))
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
                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append(
                                            (xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append(
                                            (yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append(
                                            (xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append(
                                            (yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.15 * np.sin(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 135))))
                                        y11.append((yyyyy[aux] + 0.15 * np.cos(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 135))))
                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))
                                    elif arqi.wspd[iwdir] > 27 and arqi.wspd[iwdir] <= 32:
                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append(
                                            (xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append(
                                            (yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append(
                                            (xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append(
                                            (yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.21 * np.sin(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y11.append((yyyyy[aux] + 0.21 * np.cos(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 120))))

                                        x12.append((xxxx[gg]))
                                        y12.append((yyyy[ggg]))
                                        x13.append((xxxx[gg]))
                                        y13.append((yyyy[ggg]))
                                    elif arqi.wspd[iwdir] > 32 and arqi.wspd[iwdir] <= 37:
                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append(
                                            (xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append(
                                            (yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append(
                                            (xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append(
                                            (yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.21 * np.sin(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y11.append((yyyyy[aux] + 0.21 * np.cos(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 120))))

                                        x12.append(
                                            (xxxx[aux] + 0.15 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y12.append(
                                            (yyyy[aux] + 0.15 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x13.append((xxxxx[aux] + 0.19 * np.sin(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 145))))
                                        y13.append((yyyyy[aux] + 0.19 * np.cos(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 145))))
                                    elif arqi.wspd[iwdir] > 37 and arqi.wspd[iwdir] <= 42:
                                        x7.append(xxxx[gg] + 0.30 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y7.append(yyyy[ggg] + 0.30 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        xxxxxx.append(
                                            (xxxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 90))))
                                        yyyyyy.append(
                                            (yyyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 90))))

                                        x8.append(xxxx[aux] + 0.25 * np.sin(np.pi / 180 * (arqi.wdir[iwdir])))
                                        y8.append(yyyy[aux] + 0.25 * np.cos(np.pi / 180 * (arqi.wdir[iwdir])))
                                        x9.append(
                                            (xxxxx[aux] + 0.2 * np.sin(np.pi / 180 * (arqi.wdir[iwdir] - 105))))
                                        y9.append(
                                            (yyyyy[aux] + 0.2 * np.cos(np.pi / 180 * (arqi.wdir[iwdir] - 105))))

                                        x10.append(
                                            (xxxx[aux] + 0.20 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y10.append(
                                            (yyyy[aux] + 0.20 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x11.append((xxxxx[aux] + 0.21 * np.sin(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 120))))
                                        y11.append((yyyyy[aux] + 0.21 * np.cos(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 120))))

                                        x12.append(
                                            (xxxx[aux] + 0.15 * np.sin(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        y12.append(
                                            (yyyy[aux] + 0.15 * np.cos(np.pi / 180 * (arqi.wdir[iwdir]))))
                                        x13.append((xxxxx[aux] + 0.24 * np.sin(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 130))))
                                        y13.append((yyyyy[aux] + 0.24 * np.cos(
                                            np.pi / 180 * (arqi.wdir[iwdir] - 130))))


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
                # show(p)
                from bokeh.embed import components

                # st.components.v1.iframe(p, height=600, width=1700, scrolling=True)
                # html = file_html(p, CDN, "my plot")
                # st.bokeh_chart(html, use_container_width=True)

                # script, div = components(p)
                #  html = template.render(resources=resources,
                #                         script=script,
                #                         div=div)

                # HtmlFile = open("SBMEtab.html", 'r', encoding='utf-8')
                from bokeh.resources import CDN
                from bokeh.embed import file_html

                handle = file_html(p, CDN, "my plot")

                # source_code = HtmlFile.read()
                source_code = handle

            # print(source_code)
            # ppp=components.html(source_code)
            # ppp = open("SBMEtab.html")
            # components.html(ppp.read())
            # PP=_data_url_to_image(p)

            # save(p)

            except Exception as err:

                print(f"Unexpected {err=}, {type(err)=}")
                source_code = ("ERRO - DADOS INCONSISTENTES - MODIFIQUE AS OPÇÕES E TENTE DE NOVO")
            return source_code
    def main_page():


        def main():


            pt1 = pd.read_csv('/mount/src/edomenico/metar_trat_teste1.csv',
                                    sep=',',
                                    decimal='.')
            pt2 = pd.read_csv('/mount/src/edomenico/metar_trat_teste2.csv',
                                    sep=',',
                                    decimal='.')

            # tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 \
            #                 , tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23, tab24 \
            #                 ,tab25, tab26, tab27, tab28 = st.tabs(
            #     ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBFS', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
            #      'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN', 'SBPL',
            #      'SBPJ'])
            area = ['Área 1', 'Área 2']
            area_1 = ['SBJR', 'SBES', 'SBME', 'SBFS', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS',
                      'SBAC', 'SBJE',
                      'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN',
                      'SBPL',
                      'SBPJ']
            area_2 = ['SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA', 'SBCJ',
                      'SBHT',
                      'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBMY', 'SBTF', 'SBUA',
                      'SBEG',
                      'SBBV', 'SSKW', 'SWEI', 'SWPI']
            start_date = datetime.today()
            end_date = datetime.today()
            start_datee = datetime.today()
            nome_estacao='N'
            with st.sidebar:
                with st.container(border=True):
                    on = st.toggle('Atualizar dados')
                    if on:
                        # st.write('Atualização dos Dados')
                        # atualizardados = st.radio('Atualizar', ['Último dia', 'Selecionar vários dias/Estação','Nenhum'], horizontal=True,index=2)

                        # if st.button('Último dia'):
                        # #if atualizardados=='Último dia':
                        #
                        #     progress_text = "Processando... Aguarde."
                        #     my_bar = st.progress(0, text=progress_text)
                        #     pt = rest(1,to_data,from_data)
                        #     my_bar.progress(50, text="Em andamento...")
                        #     # for percent_complete in range(100):
                        #     #     time.sleep(0.01)
                        #     pt = rest(2,to_data,from_data)
                        #
                        #     my_bar.progress(100, text="Terminou")
                        too_data = format(datetime.utcnow(), "%d/%m/%Y")
                        to_data = st.date_input('Inicio:', start_date)
                        from_data = st.date_input('Fim:', end_date)

                        if st.button('Selecionar'):
                            # if atualizardados=='Último dia':

                            # if st.button('Consultar'):
                            progress_text = "Processando... Aguarde."
                            my_bar = st.progress(0, text=progress_text)
                            pt = rest(1, to_data, from_data,nome_estacao)
                            my_bar.progress(50, text="Em andamento...")
                            # for percent_complete in range(100):
                            #     time.sleep(0.01)
                            pt = rest(2, to_data, from_data,nome_estacao)

                            my_bar.progress(100, text="Terminou")

                    # else:
                    st.divider()
                    on2 = st.toggle('Consultar outra data')
                    if on2:
                        # st.divider()
                        # st.write('Visualização dos dados')
                        selecionaperiodo = st.radio('Escolha o período', ['Últimos 10 dias', 'Selecionar dia inicial'],
                                                    horizontal=True)
                        if selecionaperiodo == 'Últimos 10 dias':
                            datainicial = datetime.utcnow() - timedelta(9)
                        else:
                            too_data = st.date_input('Dia Inicial:', start_datee)
                            datainicial = too_data
                        # datainicial= datainicial-timedelta(9)
                    else:
                        datainicial = datetime.utcnow() - timedelta(9)
                # st.divider()

                # st.markdown("## Atualizar Dados")

                # atualizar_horario = st.toggle('Atualizar horário')
                with st.container(border=True):
                    selarea = st.radio("Escolha a área", ["Área 1", "Área 2"], horizontal=True)

                    # col1, col2 = st.columns(2)
                    if selarea == "Área 1":
                        # with col1:
                        # st.header('Área 1')
                        nomedaestacao = st.radio("Área 1", area_1)
                        noarea = 1

                    else:
                        # st.header('Área 2')
                        nomedaestacao = st.radio("Área 2", area_2)
                        noarea = 2

                st.markdown(
                    """


                    e-mail → edomenico813@gmail.com


                    """
                )

            p = tabuleiro(nomedaestacao, noarea, datainicial,pt1,pt2)

            import streamlit.components.v1 as components

            st.components.v1.html(p, height=2300, width=1700, scrolling=True)

        st.session_state
        main()
            # from streamlit_bokeh_events import streamlit_bokeh_events
            # event_result = streamlit_bokeh_events(
            #     events="TestSelectEvent",
            #     bokeh_plot=p,
            #     key="foo",
            #     debounce_time=1000,
            # )
            # st.subheader("Raw Event Data")
            # st.write(event_result)
            # st.bokeh_chart(html_content,use_container_width=True)
            # st.write(p)

            # barra_lateral = st.sid,ebar.empty()
        # area_seleciona = st.sidebar.selectbox("Seleciona a área:", area)
        #  if st.button('Atualizar dados'):
        #      pt = rest(noarea)
        #      ll=1
        # st.write('Atualizar os dados')
        # escolha= st.radio('Atualizar os dados',["Sim","Não"],index=1,horizontal=True)

        # time.sleep(1)
        # my_bar.empty()

        # escolha.index='None'
        

        # if __name__ == '__main__':
        #     if runtime.exists():
        #         main()
        #     else:
        #         sys.argv = ["streamlit", "run", sys.argv[0]]
        #         sys.exit(stcli.main())
    def page2():
        pt1 = pd.read_csv('/mount/src/edomenico/metar_trat_teste1.csv',
                                    sep=',',
                                    decimal='.')
        pt2 = pd.read_csv('/mount/src/edomenico/metar_trat_teste2.csv',
                                    sep=',',
                                    decimal='.')
        st.markdown("# Page 2 ❄️")
        start_date = datetime.today()
        end_date = datetime.today()
        #to_date = datetime.today()
        title=''
        entrou=0
        with st.sidebar:
            title = st.text_input('Escolha a estação', 'SBMQ')

            st.write('Escolha o período para visualizar')
            to_data = st.date_input('Inicio:', start_date)
            datai=to_data
            from_data = st.date_input('Fim:', end_date)
            if st.button('Iniciar'):
                progress_text = "Processando... Aguarde."
                my_bar = st.progress(0, text=progress_text)
                pt = rest(1, to_data, from_data, title)
                my_bar.progress(100, text="Terminou...")
                entrou=1
        #if entrou==1:
        p = tabuleiro(title, 2, datai,pt1,pt2)

        import streamlit.components.v1 as components

        st.components.v1.html(p, height=2300, width=1700, scrolling=True)

        st.markdown("# Page 2 ❄️")
        

    def page3():
        def rosa():
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
          import os
          import glob
      
      
          from PIL import Image
          def nomeestacao(nome):
              if nome=='SBJR':
                  nomeaerodromo="Aeródromo de Jacarepaguá(RJ)"
              elif nome=='SBES':
                  nomeaerodromo = "Aeródromo de São Pedro da Aldeia(RJ)"
              elif nome=='SBME':
                  nomeaerodromo = "Aeródromo de Macaé(RJ)"
              elif nome=='SBFS':
                  nomeaerodromo = "Aeródromo de São Tomé(RJ)"
              elif nome=='SBCP':
                  nomeaerodromo = "Aeródromo de Campos dos Goytacazes(RJ)"
              elif nome=='SBRJ':
                  nomeaerodromo = "Aeródromo do Rio de Janeiro - Santos Dumont(RJ)"
              elif nome=='SBCB':
                  nomeaerodromo = "Aeródromo de Cabo Frio(RJ)"
              elif nome=='SBVT':
                  nomeaerodromo = "Aeródromo de Vitória(ES)"
              elif nome=='SBPS':
                  nomeaerodromo = "Aeródromo de Porto Seguro(BA)"
              elif nome=='SBGL':
                  nomeaerodromo = "Aeródromo do Rio de Janeiro - Galeão(RJ)"
              elif nome=='SBNT':
                  nomeaerodromo = "Aeródromo de Natal(RN)"
              elif nome=='SBMS':
                  nomeaerodromo = "Aeródromo de Mossoró(RN)"
              elif nome=='SBAC':
                  nomeaerodromo = "Aeródromo de Aracati(CE)"
              elif nome=='SBJE':
                  nomeaerodromo = "Aeródromo de Jericoacoara(CE)"
              elif nome=='SBPB':
                  nomeaerodromo = "Aeródromo de Parnaíba(PI)"
              elif nome=='SBAR':
                  nomeaerodromo = "Aeródromo de Aracaju(SE)"
              elif nome=='SBMO':
                  nomeaerodromo = "Aeródromo de Maceió(AL)"
              elif nome=='SBRF':
                  nomeaerodromo = "Aeródromo de Recife(PE)"
              elif nome=='SBJP':
                  nomeaerodromo = "Aeródromo de João Pessoa(PB)"
              elif nome=='SBSG':
                  nomeaerodromo = "Aeródromo de São Gonçalo(RN)"
              elif nome=='SBFZ':
                  nomeaerodromo = "Aeródromo de Fortaleza(CE)"
              elif nome=='SBSL':
                  nomeaerodromo = "Aeródromo de São Luis(MA)"
              elif nome=='SBTE':
                  nomeaerodromo = "Aeródromo de Teresina(PI)"
              elif nome=='SBJU':
                  nomeaerodromo = "Aeródromo de Juazeiro do Norte(CE)"
              elif nome=='SBKG':
                  nomeaerodromo = "Aeródromo de Campina Grande(PB)"
              elif nome=='SBFN':
                  nomeaerodromo = "Aeródromo de Fernando de Noronha(PE)"
              elif nome=='SBPL':
                  nomeaerodromo = "Aeródromo de Petrolina(PE)"
              elif nome=='SBPJ':
                  nomeaerodromo = "Aeródromo de Palmas(PJ)"
              elif nome == 'SBRD':
                  nomeaerodromo = "Aeródromo de Rondonópolis(MT)"
              elif nome == 'SBVH':
                  nomeaerodromo = "Aeródromo de Vilhena(RO)"
              elif nome == 'SBJI':
                  nomeaerodromo = "Aeródromo de Ji-Paraná(RO)"
              elif nome == 'SBRB':
                  nomeaerodromo = "Aeródromo de Rio Branco(AC)"
              elif nome == 'SSKW':
                  nomeaerodromo = "Aeródromo de Cacoal(RO)"
              elif nome == 'SBCY':
                  nomeaerodromo = "Aeródromo de Cuiabá(MT)"
              elif nome == 'SBPV':
                  nomeaerodromo = "Aeródromo de Porto Velho(RO)"
              elif nome == 'SBCZ':
                  nomeaerodromo = "Aeródromo de Cruzeiro do Sul(AC)"
              elif nome == 'SBTT':
                  nomeaerodromo = "Aeródromo de Tabatinga(AM)"
              elif nome == 'SBIZ':
                  nomeaerodromo = "Aeródromo de Imperatriz(MA)"
              elif nome == 'SBCI':
                  nomeaerodromo = "Aeródromo de Carolina(MA)"
              elif nome == 'SBMA':
                  nomeaerodromo = "Aeródromo de Marabá(PA)"
              elif nome == 'SBCJ':
                  nomeaerodromo = "Aeródromo de Carajás(PA)"
              elif nome == 'SBHT':
                  nomeaerodromo = "Aeródromo de Altamira(PA)"
              elif nome == 'SBTB':
                  nomeaerodromo = "Aeródromo de Trombetas(PA)"
              elif nome == 'SBOI':
                  nomeaerodromo = "Aeródromo de Oiapoque(AP)"
              elif nome == 'SBBE':
                  nomeaerodromo = "Aeródromo de Belém(PA)"
              elif nome == 'SBMQ':
                  nomeaerodromo = "Aeródromo de Macapá(AP)"
              elif nome == 'SBSN':
                  nomeaerodromo = "Aeródromo de Santarém(PA)"
              elif nome == 'SBSO':
                  nomeaerodromo = "Aeródromo de Sorriso(MT)"
              elif nome == 'SBSI':
                  nomeaerodromo = "Aeródromo de Sinop(MT)"
              elif nome == 'SBAT':
                  nomeaerodromo = "Aeródromo de Alta Floresta(MT)"
              elif nome == 'SBIH':
                  nomeaerodromo = "Aeródromo de Itaituba(PA)"
              elif nome == 'SBMY':
                  nomeaerodromo = "Aeródromo de Manicoré(AM)"
              elif nome == 'SWPI':
                  nomeaerodromo = "Aeródromo de Parintins(AM)"
              elif nome == 'SBTF':
                  nomeaerodromo = "Aeródromo de Tefé(AM)"
          
              elif nome == 'SBUA':
                  nomeaerodromo = "Aeródromo de São Gabriel da Cachoeira(AM)"
              elif nome == 'SBEG':
                  nomeaerodromo = "Aeródromo de Eduardo Gomes(AM)"
              elif nome == 'SBBV':
                  nomeaerodromo = "Aeródromo de Boa Vista(RR)"
              elif nome == 'SWEI':
                  nomeaerodromo = "Aeródromo de Erinepé(AM)"
          
          
          
          
          
          
          
              return nomeaerodromo
          
          def eareaprevisor(defarea):
              if defarea == "Área 1":
                  area_escolhida = ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBFS','SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS',
                                      'SBAC','SBJE', 'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU',
                                      'SBKG', 'SBFN','SBPL', 'SBPJ']
              else:
                  area_escolhida = ['SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA',
                                     'SBCJ','SBHT', 'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBMY',
                                      'SBTF', 'SBUA','SBEG', 'SBBV', 'SSKW', 'SWEI', 'SWPI']
              return area_escolhida
          
          def eareausuario(defarea):
              if defarea == "Área 1":
                  area_escolhida = ['Galeão - RJ', 'Santos Dumont - RJ','Jacarepaguá - RJ', 'São Pedro da Aldeia - RJ', 'Cabo Frio - RJ','Macaé - RJ', 'Farol de São Tomé - RJ',  'Campos - RJ', 'Vitória - ES',
                                    'Porto Seguro - BA', 'Natal - RN', 'São Gonçalo do Amarante - RN',
                                      'Mossoró - RN','Fortaleza - CE',' Aracati - CE','Jericoacoara - CE', 'Aracaju - SE',
                                    'Maceió - AL', 'Recife - PE', 'Petrolina - PE', 'Fernando de Noronha - PE','João Pessoa - PB', 'Campina Grande - PB','Juazeiro do Norte - PB',
                                      'São Luis - MA', 'Teresina - PI', 'Parnaíba - PI','Palmas - TO']
              else:
                  area_escolhida =['Cuiabá - MT', 'Rondonópolis - MT','Sorriso - MT','Sinop -MT','Alta Floresta - MT',
                                   'Porto Velho - RO', 'Vilhena - RO','Cacoal - RO',' Ji-Paraná - RO', 'Rio Branco - AC',
                                   'Cruzeiro do Sul - AC','Eduardo Gomes - AM', 'Tabatinga - AM','São Gabriel da Cachoeira - AM'
                                   'Tefé - AM','Eurinepé - AM', 'Manicoré - AM', 'Parintins - AM','Imperatriz - MA','Carolina - MA',
                                   'Belém - PA','Santarém - PA','Trombetas - PA', 'Itaituba - PA','Carajás - PA','Marabá - PA',
                                   'Altamira - PA','Macapá - AP', 'Oiapoque - AP','Boa Vista -RR' ]
              return area_escolhida
          
          def sigla(est):
              if est=='Galeão - RJ':
                  sigl= 'SBGL'
              elif est== 'Santos Dumont - RJ':
                  sigl='SBRJ'
              elif est =='Jacarepaguá - RJ':
                  sigl='SBJR'
              elif est== 'São Pedro da Aldeia - RJ':
                  sigl='SBES'
              elif est== 'Cabo Frio - RJ':
                  sigl='SBCB'
              elif est=='Macaé - RJ':
                  sigl='SBME'
              elif est== 'Farol de São Tomé - RJ':
                  sigl='SBFS'
              elif est=='Campos - RJ':
                  sigl='SBCP'
              elif est == 'Vitória - ES':
                  sigl = 'SBVT'
              elif est == 'Porto Seguro - BA':
                  sigl = 'SBPS'
              elif est == 'Natal - RN':
                  sigl = 'SBNT'
              elif est == 'São Gonçalo do Amarante - RN':
                  sigl = 'SBSG'
              elif est == 'Mossoró - RN':
                  sigl = 'SBMS'
              elif est == 'Fortaleza - CE':
                  sigl = 'SBFZ'
              elif est == 'Aracati - CE':
                  sigl = 'SBAC'
              elif est == 'Jericoacoara - CE':
                  sigl = 'SBJE'
              elif est == 'Aracaju - SE':
                  sigl = 'SBAR'
              elif est == 'Maceió - AL':
                  sigl = 'SBMO'
              elif est == 'Recife - PE':
                  sigl = 'SBRF'
              elif est == 'Petrolina - PE':
                  sigl = 'SBPL'
          
              elif est == 'Fernando de Noronha - PE':
                  sigl = 'SBFN'
              elif est == 'João Pessoa - PB':
                  sigl = 'SBJP'
              elif est == 'Campina Grande - PB':
                  sigl = 'SBKG'
              elif est == 'Juazeiro do Norte - PB':
                  sigl = 'SBJU'
              elif est == 'São Luis - MA':
                  sigl = 'SBSL'
          
              elif est == 'Teresina - PI':
                  sigl = 'SBTE'
              elif est == 'Parnaíba - PI':
                  sigl = 'SBPB'
          
              elif est == 'Palmas - TO':
                  sigl = 'SBPJ'
          
          
          
              elif est== 'Cuiabá - MT':
                  sigl='SBCY'
              elif est =='Rondonópolis - MT':
                  sigl='SBRD'
              elif est== 'Sinop -MT':
                  sigl='SBSI'
              elif est== 'Alta Floresta - MT':
                  sigl='SBAT'
              elif est == 'Sorriso - MT':
                  sigl = 'SBSO'
              elif est=='Porto Velho - RO':
                  sigl = 'SBPV'
          
              elif est== 'Vilhena - RO':
                  sigl='SBVH'
              elif est =='Cacoal - RO':
                  sigl='SSKW'
              elif est== 'Ji-Paraná - RO':
                  sigl='SBJI'
              elif est== 'Rio Branco - AC':
                  sigl='SBRB'
              elif est=='Cruzeiro do Sul - AC':
                  sigl = 'SBCZ'
          
              elif est== 'Eduardo Gomes - AM':
                  sigl='SBEG'
              elif est =='Tabatinga - AM':
                  sigl='SBTT'
              elif est== 'São Gabriel da Cachoeira - AM':
                  sigl='SBUA'
              elif est== 'Tefé - AM':
                  sigl='SBTF'
              elif est=='Eurinepé - AM':
                  sigl = 'SWEI'
          
              elif est== 'Manicoré - AM':
                  sigl='SBMY'
              elif est =='Parintins - AM':
                  sigl='SWPI'
              elif est== 'Imperatriz - MA':
                  sigl='SBIZ'
              elif est== 'Carolina - MA':
                  sigl='SBCI'
              elif est=='Belém - PA':
                  sigl = 'SBBE'
          
              elif est== 'Santarém - PA':
                  sigl='SBSN'
              elif est =='Trombetas - PA':
                  sigl='SBTB'
              elif est== 'Itaituba - PA':
                  sigl='SBIH'
              elif est== 'Carajás - PA':
                  sigl='SBCJ'
              elif est=='Marabá - PA':
                  sigl = 'SBMA'
          
              elif est == 'Altamira - PA':
                  sigl = 'SBIH'
              elif est == 'Macapá - AP':
                  sigl = 'SBMQ'
              elif est == 'Oiapoque - AP':
                  sigl = 'SBOI'
              elif est == 'Boa Vista -RR':
                  sigl = 'SBBV'
          
          
              return sigl
          
          
          
          
          
          
          
          def main():
          
          
          
              def wind_dir_speed_freq(boundary_lower_speed, boundary_higher_speed, boundary_lower_direction,
                                      boundary_higher_direction,wind_rose_data):
                  # mask for wind speed column
                  log_mask_speed = (wind_rose_data[:, 0] >= boundary_lower_speed) & (wind_rose_data[:, 0] < boundary_higher_speed)
                  # mask for wind direction
                  log_mask_direction = (wind_rose_data[:, 1] >= boundary_lower_direction) & (
                          wind_rose_data[:, 1] < boundary_higher_direction)
          
                  # application of the filter on the wind_rose_data array
                  return wind_rose_data[log_mask_speed & log_mask_direction]
              def rosa(nomeestacaorosa,hora,area,frequencia,estacaodoano,mesdoano,horaria):
                  #area_value ='ÁREA 2'
                  nomeest=nomeestacaorosa
                  # if area_value == 'ÁREA 2':
                  #     arqi1 = pd.read_csv('metar_trat_teste2.csv')
                  # else:
                  #     arqi1 = pd.read_csv('metar_trat_teste1.csv')
          
          
                  if area==1:
                      os.chdir("/mount/src/edomenico/area1")
                      #os.chdir("C:/Users/edome/OneDrive/Área de Trabalho/similaridade/area1")
                      # extension = 'csv'
                      # all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
                      # arqi1 = pd.concat([pd.read_csv(f) for f in all_filenames])
                      #arqi1 = pd.read_csv('metar_trat_teste1.csv')
          
          
                  else:
                      os.chdir("/mount/src/edomenico/area2")
                      #os.chdir("C:/Users/edome/OneDrive/Área de Trabalho/similaridade/area2")
                  extension = 'csv'
                  all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
                  arqi1 = pd.concat([pd.read_csv(f) for f in all_filenames])
                  testea=pd.read_csv(all_filenames[1])
                  testea.to_csv('/mount/src/edomenico/nome_do_arquivo.csv')
          # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                 # nomeest="SBJR"
                 # hora=6
          #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                  arqi = arqi1.loc[(arqi1['estacao'] == nomeest)]
                  arqi = arqi.reset_index(drop=True)
                  xr = []
                  for i in range(0, len(arqi['datahora']), 1):
                      p = arqi.datahora[i]
          
                      xr.append(int(p[11:13]))
                  arqi['hora'] = xr
                  if horaria == True:
                      arqi = arqi.loc[(arqi['hora'] == hora)]
          
                  x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in arqi.datahora]
                  # da=x.month
                  arqi['data_hora'] = x
                  arqi = arqi.reset_index(drop=True)
          #         if len(arqi) == 0:
          #             # ---------------------------------------------------------------------------------------------------------
          #
          #
          # #        --------------------------------------------------------------------------------------------------------
          #             img = Image.open('sem-dados-pasta.jpg')
          #             fig = px.imshow(img)
          #             #fig = plt.imread('brasil2.png')
          #             #fig = img.imread('brasil2.png')
          #             #plt.imshow(fig)fig = px.imshow(img_rgb)
                  arqzerado = 1
          
                  if len(arqi) < 10:
                      dado= [[np.nan , np.nan]]
                      totaldados=0
          
                      dfzerado = pd.DataFrame(dado, columns=['ws', 'wd'])
                      arqzerado=0
                      inicio='Estação fechada neste horário'
                      fim='Estação fechada neste horário'
                  else:
                      #inicio = arqi.datahora[0]
          
                      #fim = arqi.datahora[len(arqi) - 1]
          
                      if frequencia=="Todos os dados":
                         # arqi = arqi.loc[(arqi['data_hora'] >= '2021-01-01 00:00:00')]
                          arqi=arqi
                      elif frequencia=="Sazonal":
                          if estacaodoano=='Verão':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 12) | (arqi['data_hora'].dt.month <3)]
                          elif estacaodoano=='Outono':
                              arqi = arqi.loc[(arqi['data_hora']. dt.month >= 3) & (arqi['data_hora'].dt.month < 6)]
                          elif estacaodoano == 'Inverno':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month >= 6) & (arqi['data_hora'].dt.month < 9)]
                          elif estacaodoano == 'Primavera':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month >= 9) & (arqi['data_hora'].dt.month < 12)]
                      elif frequencia == "Mensal":
                          if mesdoano=='JAN':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month ==1)]
                          elif mesdoano=='FEV':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 2)]
                          elif mesdoano=='MAR':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 3)]
                          elif mesdoano=='ABR':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 4)]
          
                          elif mesdoano=='MAI':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 5)]
                          elif mesdoano=='JUN':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 6)]
                          elif mesdoano=='JUL':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 7)]
          
                          elif mesdoano=='AGO':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 8)]
                          elif mesdoano=='SET':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 9)]
                          elif mesdoano=='OUT':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 10)]
                          elif mesdoano=='NOV':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 11)]
                          elif mesdoano=='DEZ':
                              arqi = arqi.loc[(arqi['data_hora'].dt.month == 12)]
          
          
          
          
                      arqi.sort_values(by=['data_hora'], inplace=True)
          
                      arqi = arqi.reset_index(drop=True)
                      if len(arqi) < 10:
                          dado = [[np.nan, np.nan]]
                          totaldados = 0
          
                          dfzerado = pd.DataFrame(dado, columns=['ws', 'wd'])
                          arqzerado = 0
                          inicio = 'Estação fechada neste horário'
                          fim = 'Estação fechada neste horário'
                      else:
                          inicio = arqi.data_hora[0]
                          fim = arqi.data_hora[len(arqi) - 1]
                          arqi['ws'] = arqi['wspd']
                          arqi['wd'] = arqi['wdir']
                          totaldados=len(arqi)
          
                  wind_rose_df = pd.DataFrame(np.zeros((16 * 9, 3)), index=None,
                                              columns=('direction', 'strength', 'frequency'))
          
                  directions = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW',
                                'NNW']
                  directions_deg = np.array(
                      [0, 22.5, 45, 72.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270, 292.5, 315, 337.5])
                  speed_bins = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-12', '12-14', '14-16', '>16']
          
                  # filling in the dataframe with directions and speed bins
                  wind_rose_df.direction = directions * 9
                  wind_rose_df.strength = np.repeat(speed_bins, 16)
          
                  # creating a multiindex dataframe with frequencies
          
                  idx = pd.MultiIndex.from_product([speed_bins,
                                                    directions_deg],
                                                   names=['wind_speed_bins', 'wind_direction_bins'])
                  col = ['frequency']
                  frequencies_df = pd.DataFrame(0, idx, col)
                  if len(arqi) >10:
                      df1 = arqi
                  else:
                      dado = [[np.nan, np.nan]]
                      totaldados = 0
          
                      dfzerado = pd.DataFrame(dado, columns=['ws', 'wd'])
                      arqzerado = 0
                      df1=dfzerado
                  if len(df1) != 0:
                      # print(df1.ws[:],df1.wd[:])
                      wind_rose_data = df1[['ws', 'wd']].to_numpy()
          
                      # distance between the centre of the bin and its edge
                      step = 11.25
          
                      # converting data between 348.75 and 360 to negative
                      for i in range(len(wind_rose_data)):
                          # print(wind_rose_data[i, 1])
                          if directions_deg[-1] + step <= wind_rose_data[i, 1] and wind_rose_data[i, 1] < 360:
                              wind_rose_data[i, 1] = wind_rose_data[i, 1] - 360
          
                      # determining the direction bins
                      bin_edges_dir = directions_deg - step
                      bin_edges_dir = np.append(bin_edges_dir, [directions_deg[-1] + step])
          
                      # determining speed bins ( the last bin is 50 as above those speeds the outliers were removed for the measurements)
                      threshold_outlier_rm = 50
                      bin_edges_speed = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, threshold_outlier_rm])
          
                      frequencies = np.array([])
                      # loop selecting given bins and calculating frequencies
                      for i in range(len(bin_edges_speed) - 1):
                          for j in range(len(bin_edges_dir) - 1):
                              bin_contents = wind_dir_speed_freq(bin_edges_speed[i], bin_edges_speed[i + 1], bin_edges_dir[j],
                                                                 bin_edges_dir[j + 1], wind_rose_data)
          
                              # applying the filtering function for every bin and checking the number of measurements
                              bin_size = len(bin_contents)
                              if len(wind_rose_data) != 0:
                                  frequency = bin_size / len(wind_rose_data)
                              else:
                                  frequency = 0.0
                              # obtaining the final frequencies of bin
                              frequencies = np.append(frequencies, frequency)
          
                      # updating the frequencies dataframe
                      frequencies_df.frequency = frequencies * 100  # [%]
                      wind_rose_df.frequency = frequencies * 100  # [%]
          
                      # calling the PLOT function
                      # """
                      # PLOTTING THE ROSES
                      # """
                      aux = len(df1)
                      # fig1 = wind_rose_fig(frequencies_df,
          
                      if arqzerado==1:
                          if horaria== True:
                              nestacao=nomeestacao(nomeestacaorosa)
                              if hora<10:
                                  horas='0'+str(hora)
                              else:
                                  horas = str(hora)
                              if frequencia=='Sazonal':
                                  title = estacaodoano + ' - ' +horas + "Z"
                              elif frequencia== 'Mensal':
                                  title = mesdoano + ' - ' + horas + "Z"
                              else:
                                  title = 'Todos os dados' + ' - ' + horas + "Z"
          
                          else:
                              nestacao = nomeestacao(nomeestacaorosa)
                              if frequencia == 'Sazonal':
                                  title =  estacaodoano
                              elif frequencia == 'Mensal':
                                  title = mesdoano
                              else:
                                  title = 'Todos os dados'
          
                      else:
                          title="SEM DADOS NESTE HORÁRIO"
                      filename = 'fig_wind_rose_WRF.png'
                      open_bool = False
                      # fig2 = wind_rose_fig(frequencies_df,
                      #                               title=df2.estacao[0]+' - '+df2.datahora[0][0:11] +' a '+ df2.datahora[aux-1][0:11]+' - '+df2.datahora[0][11:16] +' a '+ df2.datahora[aux-1][11:16]+'UTC',
                      #                               filename='fig_wind_rose_WRF.png',
                      #                               open_bool=False)
          
                      fig = go.Figure()
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('0-2'), 'frequency'],
                          name='0-2',
                          marker_color='#482878'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('2-4'), 'frequency'],
                          name='2-4',
                          marker_color='#3e4989'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('4-6'), 'frequency'],
                          name='4-6',
                          marker_color='#31688e'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('6-8'), 'frequency'],
                          name='6-8',
                          marker_color='#26828e'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('8-10'), 'frequency'],
                          name='8-10',
                          marker_color='#1f9e89'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('10-12'), 'frequency'],
                          name='10-12',
                          marker_color='#35b779'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('12-14'), 'frequency'],
                          name='12-14',
                          marker_color='#6ece58'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('14-16'), 'frequency'],
                          name='14-16',
                          marker_color='#b5de2b'))
          
                      fig.add_trace(go.Barpolar(
                          r=frequencies_df.loc[('>16'), 'frequency'],
                          name='>16',
                          marker_color='#fde725'))
          
                      fig.update_traces(
                          text=['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW',
                                'NNW'])
          
                      fig.update_layout(
                          title=title,
                          title_font_size=20,
                          showlegend=True,
                          legend_title='    Int.vento(kt)',
                          title_x=0.463,
                          legend_font_size=18,
                          polar_radialaxis_ticksuffix='%',
                          polar_angularaxis_rotation=90,
                          polar_angularaxis_direction='clockwise',
                          polar_angularaxis_tickmode='array',
                          polar_angularaxis_tickvals=[0, 22.5, 45, 72.5, 90, 112.5, 135, 157.5, 180, 202.5, 225, 247.5, 270,
                                                      292.5,
                                                      315,
                                                      337.5],
                          polar_angularaxis_ticktext=['<b>N</b>', 'NNE', '<b>NE</b>', 'ENE', '<b>E</b>', 'ESE', '<b>SE</b>',
                                                      'SSE',
                                                      '<b>S</b>', 'SSW', '<b>SW</b>', 'WSW', '<b>W</b>', 'WNW', '<b>NW</b>',
                                                      'NNW'],
                          polar_angularaxis_tickfont_size=12,
                          polar_radialaxis_tickmode='linear',
                          polar_radialaxis_angle=45,
                          polar_radialaxis_tick0=5,
                          polar_radialaxis_dtick=5,
                          polar_radialaxis_tickangle=100,
                          polar_radialaxis_tickfont_size=14,
                          hovermode='closest',
                          height=600, width=800)
          
          
                  return fig,totaldados,inicio,fim
          
              import numpy as np  # np mean, np random
              import pandas as pd  # read csv, df manipulation
              import plotly.express as px  # interactive charts
              import plotly.graph_objects as go
              import streamlit as st  #
              from datetime import datetime, timedelta
              from plotly.subplots import make_subplots
              st.set_page_config(
                  page_title="Rosa dos Ventos - CMA-GL",
                  page_icon="✅",
                  layout="wide",
              )
          
              # read csv from a github repo
              #dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"
          
          
              # read csv from a URL
              # @st.experimental_memo
              # def get_data() -> pd.DataFrame:
              #     return pd.read_csv(dataset_url)
          
              st.cache(allow_output_mutation=True)
              #df = pd.read_csv('metar_trat_teste1.csv')
              # os.chdir("C:/Users/edome/OneDrive/Área de Trabalho/similaridade/arqcsv")
              # extension = 'csv'
              # all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
              # df = pd.concat([pd.read_csv(f) for f in all_filenames])
              #
              #
              # x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in df.datahora]
              # df['data_hora'] = x
              # df['period'] = df['data_hora'].dt.hour
              # df.drop(columns=["metar", "speci", "gust"], inplace=True)
              # df.sort_values(by=['data_hora'], inplace=True)
              # df = df.reset_index(drop=True)
              # dashboard title
          
          
              st.title("Rosa dos Ventos")
          
              col3,col4=st.columns(2)
              with col3:
                  usuario = st.radio("Escolha o usuário",["Previsor","Público Geral"])
              #if usuario== "Público Geral":
               #   with col4:
               #       opcaovel= st.radio("Escolha a unidade da velocidade",["kt","m/s","km/h"])
          
              # top-level filters
              selarea=st.selectbox("Selecione a área",['Área 1','Área 2'])
              if usuario =='Previsor':
                  escolhearea=eareaprevisor(selarea)
              else:
                  escolhearea = eareausuario(selarea)
          
          
          
          
              job_filter = st.selectbox("Selecione o aeródromo",  escolhearea)
              if usuario=='Público Geral':
                  job_filter=sigla(job_filter)
          
          
          
              # creating a single-element container
              placeholder = st.empty()
              col1, col2 = st.columns(2)
          
              with col1:
                  frequencia = st.radio(
                      "Escolha a frequência",
                      ["Todos os dados", "Sazonal", "Mensal"])
              if frequencia == "Sazonal":
                  with col2:
                      estacaodoano= st.radio("Escolha a estação",
                      ["Verão", "Outono", "Inverno", "Primavera"],horizontal=True)
                      horaria=st.toggle('Horário (UTC)')
              elif frequencia=="Mensal":
                  with col2:
                      mesdoano = st.radio("Escolha o mês",
                                              ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"], horizontal=True)
                      horaria = st.toggle('Horário (UTC)')
              elif frequencia=="Todos os dados":
                  with col2:
                      horaria = st.toggle('Horário (UTC)')
          
              if frequencia=="Todos os dados":
                  estacaodoano="Nenhuma"
                  mesdoano="Nenhum"
                  #horaria=False
              if frequencia == "Sazonal":
                  mesdoano="Nenhum"
                  #horaria = False
              if frequencia == "Mensal":
                  estacaodoano="Nenhuma"
                  #horaria = False
          
          
          
          
              # dataframe filter
             # df = df[df["estacao"] == job_filter]
             # df = df.reset_index(drop=True)
          
              # captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])
              # near real-time / live feed simulation
              for seconds in range(1):
                  # df["wspd_new"] = df["wspd"]
                  # df["wdir_new"] = df["wdir"]
                  # df["dryt_new"] = df["dryt"]
          
          
                  nomeestacaorosa = job_filter
                  nomeest = nomeestacao(nomeestacaorosa)
          
                  # if nomeestacaorosa in area_1:
                  #     area = 1
                  # else:
                  #     area = 2
                  if selarea=='Área 1':
                      area=1
                  else:
                      area=2
                  if horaria == False:
                      st.header(nomeest)
          
                      fig0, ndados,inicio,fim = rosa(nomeestacaorosa, 0, area, frequencia, estacaodoano, mesdoano, horaria)
                      st.write(fig0)
                      st.header("Total de dados: " + str(ndados), divider='rainbow')
                      if inicio=='Estação fechada neste horário':
                          st.subheader('Fonte: METAR ---- Início: '+str(inicio)+' - Fim: '+str(fim)+' :disappointed:')
                      else:
                          st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                  elif horaria == True:
          
                      tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 \
                          , tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23, tab24 \
                          = st.tabs(
                          ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                           "19", "20", "21", "22", "23"])
          
          
                      with tab1:
                          st.header(nomeest)
                          fig1, ndados,inicio,fim = rosa(nomeestacaorosa, 0, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig1)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
          
                      with tab2:
                          st.header(nomeest)
                          fig2, ndados,inicio,fim = rosa(nomeestacaorosa, 1, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig2)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab3:
                          st.header(nomeest)
                          fig3, ndados,inicio,fim = rosa(nomeestacaorosa, 2, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig3)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab4:
                          st.header(nomeest)
                          fig4, ndados,inicio,fim = rosa(nomeestacaorosa, 3, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig4)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab5:
                          st.header(nomeest)
                          fig5, ndados,inicio,fim = rosa(nomeestacaorosa, 4, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig5)
          
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
          
                      with tab6:
                          st.header(nomeest)
                          fig6, ndados,inicio,fim = rosa(nomeestacaorosa, 5, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig6)
          
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab7:
                          st.header(nomeest)
                          fig7, ndados,inicio,fim = rosa(nomeestacaorosa, 6, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig7)
          
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab8:
                          st.header(nomeest)
                          fig8, ndados,inicio,fim = rosa(nomeestacaorosa, 7, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig8)
          
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab9:
                          st.header(nomeest)
                          fig9, ndados,inicio,fim = rosa(nomeestacaorosa, 8, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig9)
          
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab10:
                          st.header(nomeest)
                          fig10, ndados,inicio,fim = rosa(nomeestacaorosa, 9, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig10)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab11:
                          st.header(nomeest)
                          fig11, ndados,inicio,fim = rosa(nomeestacaorosa, 10, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig11)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab12:
                          st.header(nomeest)
                          fig12, ndados,inicio,fim = rosa(nomeestacaorosa, 11, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig12)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab13:
                          st.header(nomeest)
                          fig13, ndados,inicio,fim = rosa(nomeestacaorosa, 12, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig13)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab14:
                          st.header(nomeest)
                          fig14, ndados,inicio,fim = rosa(nomeestacaorosa, 13, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig14)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab15:
                          st.header(nomeest)
                          fig15, ndados,inicio,fim = rosa(nomeestacaorosa, 14, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig15)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
          
                      with tab16:
                          st.header(nomeest)
                          fig16, ndados,inicio,fim = rosa(nomeestacaorosa, 15, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig16)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab17:
                          st.header(nomeest)
                          fig17, ndados,inicio,fim = rosa(nomeestacaorosa, 16, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig17)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab18:
                          st.header(nomeest)
                          fig18, ndados,inicio,fim = rosa(nomeestacaorosa, 17, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig18)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab19:
                          st.header(nomeest)
                          fig19, ndados,inicio,fim = rosa(nomeestacaorosa, 18, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig19)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab20:
                          st.header(nomeest)
                          fig20, ndados,inicio,fim = rosa(nomeestacaorosa, 19, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig20)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab21:
                          st.header(nomeest)
                          fig21, ndados,inicio,fim = rosa(nomeestacaorosa, 20, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig21)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab22:
                          st.header(nomeest)
                          fig22, ndados,inicio,fim = rosa(nomeestacaorosa, 21, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig22)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab23:
                          st.header(nomeest)
                          fig23, ndados,inicio,fim = rosa(nomeestacaorosa, 22, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig23)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
                      with tab24:
                          st.header(nomeest)
                          fig24, ndados,inicio,fim = rosa(nomeestacaorosa, 23, area, frequencia, estacaodoano, mesdoano, horaria)
                          st.write(fig24)
                          st.header("Total de dados: " + str(ndados), divider='rainbow')
                          if inicio == 'Estação fechada neste horário':
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :disappointed:')
                          else:
                              st.subheader('Fonte: METAR ---- Início: ' + str(inicio) + ' - Fim: ' + str(fim) + ' :sunglasses:')
            st.markdown("# Page 3 🎉")
            rosa()
        #st.sidebar.markdown("# Page 3 🎉")

    page_names_to_funcs = {
        "Main Page": main_page,
        "Page 2": page2,
        "Page 3": page3,
    }

    selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
    page_names_to_funcs[selected_page]()

st.session_state
main2()
