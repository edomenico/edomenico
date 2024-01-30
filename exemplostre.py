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



from PIL import Image
def nomeestacao(nome):
    if nome=='SBJR':
        nomeaerodromo="Aeródromo de Jacarepaguá(RJ)"
    elif nome=='SBES':
        nomeaerodromo = "Aeródromo de São Pedro da Aldeia(RJ)"
    elif nome=='SBME':
        nomeaerodromo = "Aeródromo de Macaé(RJ)"


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
            arqi1 = pd.read_csv('metar_trat_teste1.csv')
        else:
            arqi1 = pd.read_csv('metar_trat_teste2.csv')

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
        arqi = arqi.loc[(arqi['hora'] == hora)]
        arqi = arqi.reset_index(drop=True)
        x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in arqi.datahora]
        # da=x.month
        arqi['data_hora'] = x
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
        arqzerado=1
        if len(arqi) == 0:
            dado= data = [[np.nan , np.nan]]
            totaldados=0

            dfzerado = pd.DataFrame(dado, columns=['ws', 'wd'])
            arqzerado=0
        else:
            if frequencia=="Anual":
                arqi = arqi.loc[(arqi['data_hora'] >= '2021-01-01 00:00:00')]
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
        if arqzerado==1:
            df1 = arqi
        else:
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
                title = str(hora) + "Z"
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

        return fig,totaldados

    import numpy as np  # np mean, np random
    import pandas as pd  # read csv, df manipulation
    import plotly.express as px  # interactive charts
    import plotly.graph_objects as go
    import streamlit as st  #
    from datetime import datetime, timedelta
    from plotly.subplots import make_subplots
    st.set_page_config(
        page_title="Real-Time Data Science Dashboard",
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
    df = pd.read_csv('metar_trat_teste1.csv')
    x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in df.datahora]
    df['data_hora'] = x
    df['period'] = df['data_hora'].dt.hour
    df.drop(columns=["metar", "speci", "gust"], inplace=True)
    df.sort_values(by=['data_hora'], inplace=True)
    df = df.reset_index(drop=True)
    # dashboard title


    st.title("Rosa dos Ventos - Horária")

    # top-level filters
    job_filter = st.selectbox("Selecione o aeródromo", pd.unique(df["estacao"]))


    # creating a single-element container
    placeholder = st.empty()
    col1, col2 = st.columns(2)

    with col1:
        frequencia = st.radio(
            "Escolha a frequência",
            ["Anual", "Sazonal", "Mensal", "Horária"])
    if frequencia == "Sazonal":
        with col2:
            estacaodoano= st.radio("Escolha a estação",
            ["Verão", "Outono", "Inverno", "Primavera"],horizontal=True)
            horaria=st.toggle('Horária')
    elif frequencia=="Mensal":
        with col2:
            mesdoano = st.radio("Escolha o mês",
                                    ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"], horizontal=True)
            horaria = st.toggle('Horária')
    elif frequencia=="Anual":
        with col2:
            horaria = st.toggle('Horária')
    else:
        horaria=True
    if frequencia=="Anual":
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
    df = df[df["estacao"] == job_filter]
    df = df.reset_index(drop=True)

    # captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])
    # near real-time / live feed simulation
    for seconds in range(1):
        df["wspd_new"] = df["wspd"]
        df["wdir_new"] = df["wdir"]
        df["dryt_new"] = df["dryt"]

        area_1 = ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC',
                  'SBJE',
                  'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN',
                  'SBPL',
                  'SBPJ']
        area_2 = ['SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA', 'SBCJ',
                  'SBHT',
                  'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBMY', 'SBTF', 'SBUA',
                  'SBEG', 'SBBV',
                  'SSKW', 'SWEI', 'SWPI']
        nomeestacaorosa = df["estacao"][0]
        if nomeestacaorosa in area_1:
            area = 1
        else:
            area = 2
        if horaria == False:
            st.header(nomeestacaorosa)
            fig1, ndados = rosa(nomeestacaorosa, 0, area, frequencia, estacaodoano, mesdoano, horaria)
            st.write(fig1)
            st.subheader("Total de dados: " + str(ndados))
        elif horaria == True:
            tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13 \
                , tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23, tab24 \
                = st.tabs(
                ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                 "19", "20", "21", "22", "23"])


            with tab1:
                st.header(nomeestacaorosa)
                fig1, ndados = rosa(nomeestacaorosa, 0, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig1)
                st.subheader("Total de dados: " + str(ndados))

            with tab2:
                st.header(nomeestacaorosa)
                fig2, ndados = rosa(nomeestacaorosa, 1, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig2)
                st.subheader("Total de dados: " + str(ndados))
            with tab3:
                st.header(nomeestacaorosa)
                fig3, ndados = rosa(nomeestacaorosa, 2, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig3)
                st.subheader("Total de dados: " + str(ndados))
            with tab4:
                st.header(nomeestacaorosa)
                fig4, ndados = rosa(nomeestacaorosa, 3, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig4)
                st.subheader("Total de dados: " + str(ndados))
            with tab5:
                st.header(nomeestacaorosa)
                fig5, ndados = rosa(nomeestacaorosa, 4, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig5)
                st.subheader("Total de dados: " + str(ndados))

            with tab6:
                st.header(nomeestacaorosa)
                fig6, ndados = rosa(nomeestacaorosa, 5, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig6)
                st.subheader("Total de dados: " + str(ndados))
            with tab7:
                st.header(nomeestacaorosa)
                fig7, ndados = rosa(nomeestacaorosa, 6, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig7)
                st.subheader("Total de dados: " + str(ndados))
            with tab8:
                st.header(nomeestacaorosa)
                fig8, ndados = rosa(nomeestacaorosa, 7, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig8)
                st.subheader("Total de dados: " + str(ndados))
            with tab9:
                st.header(nomeestacaorosa)
                fig9, ndados = rosa(nomeestacaorosa, 8, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig9)
            with tab10:
                st.header(nomeestacaorosa)
                fig10, ndados = rosa(nomeestacaorosa, 9, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig10)
                st.subheader("Total de dados: " + str(ndados))
            with tab11:
                st.header(nomeestacaorosa)
                fig11, ndados = rosa(nomeestacaorosa, 10, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig11)
                st.subheader("Total de dados: " + str(ndados))
            with tab12:
                st.header(nomeestacaorosa)
                fig12, ndados = rosa(nomeestacaorosa, 11, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig12)
                st.subheader("Total de dados: " + str(ndados))
            with tab13:
                st.header(nomeestacaorosa)
                fig13, ndados = rosa(nomeestacaorosa, 12, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig13)
                st.subheader("Total de dados: " + str(ndados))
            with tab14:
                st.header(nomeestacaorosa)
                fig14, ndados = rosa(nomeestacaorosa, 13, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig14)
                st.subheader("Total de dados: " + str(ndados))
            with tab15:
                st.header(nomeestacaorosa)
                fig15, ndados = rosa(nomeestacaorosa, 14, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig15)
                st.subheader("Total de dados: " + str(ndados))

            with tab16:
                st.header(nomeestacaorosa)
                fig16, ndados = rosa(nomeestacaorosa, 15, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig16)
                st.subheader("Total de dados: " + str(ndados))
            with tab17:
                st.header(nomeestacaorosa)
                fig17, ndados = rosa(nomeestacaorosa, 16, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig17)
                st.subheader("Total de dados: " + str(ndados))
            with tab18:
                st.header(nomeestacaorosa)
                fig18, ndados = rosa(nomeestacaorosa, 17, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig18)
                st.subheader("Total de dados: " + str(ndados))
            with tab19:
                st.header(nomeestacaorosa)
                fig19, ndados = rosa(nomeestacaorosa, 18, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig19)
                st.subheader("Total de dados: " + str(ndados))

            with tab20:
                st.header(nomeestacaorosa)
                fig20, ndados = rosa(nomeestacaorosa, 19, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig20)
                st.subheader("Total de dados: " + str(ndados))
            with tab21:
                st.header(nomeestacaorosa)
                fig21, ndados = rosa(nomeestacaorosa, 20, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig21)
                st.subheader("Total de dados: " + str(ndados))
            with tab22:
                st.header(nomeestacaorosa)
                fig22, ndados = rosa(nomeestacaorosa, 21, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig22)
                st.subheader("Total de dados: " + str(ndados))
            with tab23:
                st.header(nomeestacaorosa)
                fig23, ndados = rosa(nomeestacaorosa, 22, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig23)
                st.subheader("Total de dados: " + str(ndados))
            with tab24:
                st.header(nomeestacaorosa)
                fig24, ndados = rosa(nomeestacaorosa, 23, area, frequencia, estacaodoano, mesdoano, horaria)
                st.write(fig24)
                st.subheader("Total de dados: " + str(ndados))


if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
