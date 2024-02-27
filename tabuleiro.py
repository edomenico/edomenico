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


def main():
    def _data_url_to_image(data_url: str) -> Image:
        """Convert DataURL string to the image."""
        _, _data_url = data_url.split(";base64,")
        return Image.open(io.BytesIO(base64.b64decode(_data_url)))

    def tabuleiro(est,areatrab):
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
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                        var mapping = {1: 20, 2: 21, 3: 22, 4: 23, 5:24, 6: 25, 7: 26, 8: 27, 9: 28, 10: 1};
                                        return mapping[tick];
                                   """)

                else:

                    p.xaxis.formatter = FuncTickFormatter(code="""
                                var mapping = {1: 20, 2: 21, 3: 22, 4: 23, 5:24, 6: 25, 7: 26, 8: 27, 9: 28, 10: 29};
                                return mapping[tick];
                           """)
            if diaini == 21:
                if mesini == 2:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                        var mapping = {1: 21, 2: 22, 3: 23, 4: 24, 5:25, 6: 26, 7: 27, 8: 28, 9: 1, 10: 2};
                                        return mapping[tick];
                                   """)

                else:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                var mapping = {1: 21, 2: 22, 3: 23, 4: 24, 5:25, 6: 26, 7: 27, 8: 28, 9: 29, 10: 30};
                                return mapping[tick];
                           """)
            if diaini == 22:
                if mesini == 2:
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                        var mapping = {1: 22, 2: 23, 3: 24, 4: 25, 5:26, 6: 27, 7: 28, 8: 29, 9: 30, 10: 1};
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
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                        var mapping = {1: 23, 2: 24, 3: 25, 4: 26, 5:27, 6: 28, 7: 1, 8: 2, 9: 3, 10: 4};
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
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                           var mapping = {1: 24, 2: 25, 3: 26, 4: 27, 5:28, 6: 1, 7: 2, 8: 3, 9: 4, 10: 5};
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
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                           var mapping = {1: 25, 2: 26, 3: 27, 4: 28, 5:1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6};
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
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                               var mapping = {1: 26, 2: 27, 3: 28, 4: 1, 5:2, 6: 3, 7: 4, 8: 5, 9: 6, 10: 7};
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
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                           var mapping = {1: 27, 2: 28, 3: 1, 4: 2, 5:3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8};
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
                    p.xaxis.formatter = FuncTickFormatter(code="""
                                           var mapping = {1: 28, 2: 29, 1: 30, 2: 3, 5:4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9};
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
                if mesini == 1 or mesini == 3 or mesini == 5 or mesini == 7 or mesini == 8 or mesini == 10 or mesini == 12:
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
        #areatrab = 1  # dado entrada
        # datainicio='27/03/20'#dado entrada

        datainicio = datetime.utcnow() - timedelta(9)
        datainicio = datainicio.strftime('%d/%m/%y')

        if areatrab == 1:
          #  estacao_area = 'SBJR,SBES,SBME,SBCP,SBFS,SBRJ,SBCB,SBVT,SBPS,SBGL,SBNT,SBMS,SBAC,SBJE,SBPB,SBAR,SBMO,SBRF,SBJP,SBSG,SBFZ,SBSL,SBTE,SBJU,SBKG,SBFN,SBPL,SBPJ'
            # estacao_area = 'SBFZ,'
            arqi1 = pd.read_csv('metar_trat_teste1.csv')
        else:

            #estacao_area = 'SBRD,SBVH,SWEI,SBJI,SBRB,SSKW,SBCY,SBPV,SBCZ,SBTT,SBIZ,SBCI,SBMA,SBCJ,SBHT,SBTB,SBOI,SBBE,SBMQ,SBSN,SBSO,SBSI,SBAT,SBIH,SBMY,SWPI,SBTF,SBUA,SBEG,SBBV'  # sem SBMY SBCY
            # estacao_area = 'SBVH'
            # estacao_area ='SBEG,'
            arqi1 = pd.read_csv('metar_trat_teste2.csv')
        estacao_area=est
        noestacao = estacao_area.split(',')

        for i in range(0, 1, 1):
            try:
                print('nome da estação: ', noestacao[i])
                nome_estacao = noestacao[i]
                arqi = arqi1.loc[(arqi1['estacao'] == nome_estacao)]
                arqi = arqi.reset_index(drop=True)
               
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
                    dia_fim = '30'
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

                            dia.append(29 - deltatempo)
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
                    if int(arqi['vis'][inuv]) == 99 and arqi['qn1'][inuv] == "" and arqi['tp'][inuv] == "" and arqi['qncb'][
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
                print('CHEGUEI AQUI')

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





            except Exception as err:
                
                print(f"Unexpected {err=}, {type(err)=}")
            return source_code

    # tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 \
    #                 , tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23, tab24 \
    #                 ,tab25, tab26, tab27, tab28 = st.tabs(
    #     ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBFS', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
    #      'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN', 'SBPL',
    #      'SBPJ'])
    area = ['Área 1', 'Área 2']
    area_1 = ['SBJR', 'SBES', 'SBME', 'SBFS', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
              'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN', 'SBPL',
              'SBPJ']
    area_2 = ['SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA', 'SBCJ', 'SBHT',
              'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBMY', 'SBTF', 'SBUA', 'SBEG',
              'SBBV',
              'SSKW', 'SWEI', 'SWPI']
    start_date = datetime.today() - timedelta(days=365)
    end_date = datetime.today()
    with st.sidebar:
        #st.markdown("## Atualizar Dados")

        atualizar_horario = st.toggle('Atualizar horário')
        selarea = st.radio("Escolha a área",["Área 1", "Área 2"])

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
    p=tabuleiro(nomedaestacao,noarea)

    import streamlit.components.v1 as components


    st.components.v1.html(p,  height=600,width=1700, scrolling=True)
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

    #barra_lateral = st.sid,ebar.empty()
   # area_seleciona = st.sidebar.selectbox("Seleciona a área:", area)
if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
