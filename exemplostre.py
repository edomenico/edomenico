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

if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())




































































































