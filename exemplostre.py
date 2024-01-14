import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import sys
#from streamlit import cli as stcli
from streamlit.web import cli as stcli
import streamlit
from PIL import Image
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
    def rosa(nomeestacaorosa,hora,area):
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
        if len(arqi) == 0:
            # ---------------------------------------------------------------------------------------------------------


#        --------------------------------------------------------------------------------------------------------
            img = Image.open('sem-dados-pasta.jpg')
            fig = px.imshow(img)
            #fig = plt.imread('brasil2.png')
            #fig = img.imread('brasil2.png')
            #plt.imshow(fig)fig = px.imshow(img_rgb)
        else:
            arqi = arqi.loc[(arqi['data_hora'] >= '2021-01-01 00:00:00')]

            arqi.sort_values(by=['data_hora'], inplace=True)
            arqi = arqi.reset_index(drop=True)
            arqi['ws'] = arqi['wspd']
            arqi['wd'] = arqi['wdir']

            wind_rose_df = pd.DataFrame(np.zeros((16 * 9, 3)), index=None, columns=('direction', 'strength', 'frequency'))

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
            df1=arqi

            if len(df1) !=0:
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
                                                           bin_edges_dir[j + 1],wind_rose_data)

                        # applying the filtering function for every bin and checking the number of measurements
                        bin_size = len(bin_contents)
                        if len(wind_rose_data) !=0:
                            frequency = bin_size / len(wind_rose_data)
                        else:
                            frequency=0.0
                        # obtaining the final frequencies of bin
                        frequencies = np.append(frequencies, frequency)

                # updating the frequencies dataframe
                frequencies_df.frequency = frequencies * 100  # [%]
                wind_rose_df.frequency = frequencies * 100  # [%]

                # calling the PLOT function
                #"""
                #PLOTTING THE ROSES
               # """
                aux = len(df1)
                # fig1 = wind_rose_fig(frequencies_df,
                title = str(hora)+"Z"
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


        return fig


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

    # dataframe filter
    df = df[df["estacao"] == job_filter]
    df = df.reset_index(drop=True)
    # near real-time / live feed simulation
    for seconds in range(200):
        df["wspd_new"] = df["wspd"]
        df["wdir_new"] = df["wdir"]
        df["dryt_new"] = df["dryt"]

        # creating KPIs
        avg_wspd = np.mean(df["wspd_new"])
        avg_dryt = np.mean(df["dryt_new"])

        # count_married = int(
        #     df[(df["marital"] == "married")]["marital"].count()
        #     + np.random.choice(range(1, 30))
        # )

        avg_wdir = np.mean(df["wdir_new"])

        with placeholder.container():
            # # create three columns
            # kpi1, kpi2, kpi3 = st.columns(3)
            #
            # # fill in those three columns with respective metrics or KPIs
            # kpi1.metric(
            #     label="Int vento(kt) ⏳",
            #     value=round(avg_wspd),
            #     delta=round(avg_wspd) - 10,
            # )
            #
            # kpi2.metric(
            #     label="Temperatura(°C) 💍",
            #     value=round(avg_dryt),
            #     delta=round(avg_dryt) - 10,
            # )
            #
            # kpi3.metric(
            #     label="Direção do vento ＄",
            #     value=round(avg_wdir),
            #     delta=round(avg_wdir) - 10,
            # )

            # create two columns for charts
            #fig_col1, fig_col2 , fig_col3= st.columns(3)

            #fig_col1, fig_col2 , fig_col3, fig_col4= st.columns(4)
            # with fig_col1:
            #     st.markdown("### Gráfico 1")
            #
            #     fig = go.Figure(go.Histogram2dContour(
            #         x=df["period"],
            #         y=df["altn1"],
            #         colorscale='Jet',
            #         contours=dict(
            #             showlabels=True,
            #             labelfont=dict(
            #                 family='Raleway',
            #                 color='white'
            #             )
            #         ),
            #         hoverlabel=dict(
            #             bgcolor='white',
            #             bordercolor='black',
            #             font=dict(
            #                 family='Raleway',
            #                 color='black'
            #             )
            #         )
            #
            #     ))
            #     fig.update_xaxes(title_text="hora")
            #     fig.update_yaxes(title_text="altura nuvens baixas(ft)")
            #
            #
            #
            #     st.write(fig)

            # with fig_col2:
            #     st.markdown("### Gráfico 2")
            #     fig2 = px.histogram(data_frame=df, x="dryt")
            #
            #     st.write(fig2)
            #
            # st.markdown("### Dados metar descodificado")
            # st.dataframe(df)
            # time.sleep(1)

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


            tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13\
            ,tab14, tab15, tab16, tab17, tab18, tab19, tab20, tab21, tab22, tab23, tab24\
                = st.tabs(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"])
            nomeestacaorosa = df["estacao"][0]
            if nomeestacaorosa in area_1:
                area =1
            else:
                area=2
            with tab1:
                st.header(nomeestacaorosa)
                fig1=rosa(nomeestacaorosa,0,area)
                st.write(fig1)


            with tab2:
                st.header(nomeestacaorosa)
                fig2=rosa(nomeestacaorosa,1,area)
                st.write(fig2)

            with tab3:
                st.header(nomeestacaorosa)
                fig3 = rosa(nomeestacaorosa, 2,area)
                st.write(fig3)

            with tab4:
                st.header(nomeestacaorosa)
                fig4 = rosa(nomeestacaorosa, 3,area)
                st.write(fig4)

            with tab5:
                st.header(nomeestacaorosa)
                fig5 = rosa(nomeestacaorosa, 4,area)
                st.write(fig5)

            with tab6:
                st.header(nomeestacaorosa)
                fig6 = rosa(nomeestacaorosa, 5,area)
                st.write(fig6)

            with tab7:
                st.header(nomeestacaorosa)
                fig7 = rosa(nomeestacaorosa, 6,area)
                st.write(fig7)

            with tab8:
                st.header(nomeestacaorosa)
                fig8 = rosa(nomeestacaorosa, 7,area)
                st.write(fig8)

            with tab9:
                st.header(nomeestacaorosa)
                fig9 = rosa(nomeestacaorosa, 8,area)
                st.write(fig9)
            with tab10:
                st.header(nomeestacaorosa)
                fig10 = rosa(nomeestacaorosa, 9,area)
                st.write(fig10)
            with tab11:
                st.header(nomeestacaorosa)
                fig11 = rosa(nomeestacaorosa, 10,area)
                st.write(fig11)

            with tab12:
                st.header(nomeestacaorosa)
                fig12 = rosa(nomeestacaorosa, 11,area)
                st.write(fig12)

            with tab13:
                st.header(nomeestacaorosa)
                fig13 = rosa(nomeestacaorosa, 12,area)
                st.write(fig13)

            with tab14:
                st.header(nomeestacaorosa)
                fig14 = rosa(nomeestacaorosa, 13,area)
                st.write(fig14)

            with tab15:
                st.header(nomeestacaorosa)
                fig15 = rosa(nomeestacaorosa, 14,area)
                st.write(fig15)

            with tab16:
                st.header(nomeestacaorosa)
                fig16 = rosa(nomeestacaorosa, 15,area)
                st.write(fig16)

            with tab17:
                st.header(nomeestacaorosa)
                fig17 = rosa(nomeestacaorosa, 16,area)
                st.write(fig17)

            with tab18:
                st.header(nomeestacaorosa)
                fig18 = rosa(nomeestacaorosa, 17,area)
                st.write(fig18)
            with tab19:
                st.header(nomeestacaorosa)
                fig19 = rosa(nomeestacaorosa, 18,area)
                st.write(fig19)

            with tab20:
                st.header(nomeestacaorosa)
                fig20 = rosa(nomeestacaorosa, 19,area)
                st.write(fig20)
            with tab21:
                st.header(nomeestacaorosa)
                fig21 = rosa(nomeestacaorosa, 20,area)
                st.write(fig21)
            with tab22:
                st.header(nomeestacaorosa)
                fig22 = rosa(nomeestacaorosa, 21,area)
                st.write(fig22)
            with tab23:
                st.header(nomeestacaorosa)
                fig23 = rosa(nomeestacaorosa, 22,area)
                st.write(fig23)
            with tab24:
                st.header(nomeestacaorosa)
                fig24 = rosa(nomeestacaorosa, 23,area)
                st.write(fig24)

if __name__ == '__main__':
    #if streamlit._is_running_with_streamlit:
    main()
    #else:
    #    sys.argv = ["streamlit", "run", sys.argv[0]]
    #    #app.run_server(debug=True, port=8881)
      #  sys.exit(stcli.main())
