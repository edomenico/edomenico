# import pandas as pd
# from datetime import datetime,timedelta
# import plotly.graph_objects as go
# import streamlit as st
#
# area=['Área 1', 'Área 2']
# area_1= ['SBJR','SBES','SBME','SBCP','SBRJ','SBCB','SBVT','SBPS','SBGL','SBNT','SBMS','SBAC','SBJE','SBPB','SBAR','SBMO','SBRF','SBJP','SBSG','SBFZ','SBSL','SBTE','SBJU','SBKG','SBFN','SBPL','SBPJ']
# area_2= ['SBRD','SBVH','SBJI','SBRB','SBCY','SBPV','SBCZ','SBTT','SBIZ','SBCI','SBMA','SBCJ','SBHT','SBTB','SBOI','SBBE','SBMQ','SBSN','SBSO','SBSI','SBAT','SBIH','SBTF','SBUA','SBEG','SBBV','SSKW']
# start_date=datetime.today()-timedelta(days=365)
# end_date=datetime.today()
#
# def consulta_dado_grafico(estacao,datainicio,datafim):
#
#     hhhh=kkkk
#
#
# barra_lateral=st.sidebar.empty()
# area_seleciona=st.sidebar.selectbox("Seleciona a área:",area)
# if area_seleciona=='Área 1':
#     areasel=area_1
# else:
#     areasel = area_2
# estacao_seleciona=st.sidebar.selectbox("Seleciona o Aeródromo",areasel)

import sys
#from streamlit import cli as stcli
from streamlit.web import cli as stcli
import streamlit





def main():
    import pandas as pd
    from datetime import datetime, timedelta
    import plotly.graph_objects as go
    import streamlit as st
    import numpy as np
    from plotly.subplots import make_subplots

    area = ['Área 1', 'Área 2']
    area_1 = ['SBJR', 'SBES', 'SBME', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS', 'SBAC', 'SBJE',
              'SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SBFN', 'SBPL',
              'SBPJ']
    area_2 = ['SBRD', 'SBVH', 'SBJI', 'SBRB', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SBCI', 'SBMA', 'SBCJ', 'SBHT',
              'SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SBTF', 'SBUA', 'SBEG', 'SBBV',
              'SSKW']
    start_date = datetime.today() - timedelta(days=365)
    end_date = datetime.today()

    intervalo=['Diário','Mensal','Sazonal','Anual']

    @st.cache(allow_output_mutation=True)
   # @st.cache(allow_output_mutation=True)
   

    def consulta_dado_grafico(areasel,estacao, datainicio, datafim,area):
        if area == 'Área 2':
            arqi1 = pd.read_csv('metar_trat_teste2.csv')
        else:
            arqi1 = pd.read_csv('metar_trat_teste1.csv')
        arqi1['u'] = -arqi1.wspd * np.sin(np.pi / 180 * arqi1.wdir)
        arqi1['v'] = -arqi1.wspd * np.cos(np.pi / 180 * arqi1.wdir)

        arqi = arqi1.loc[(arqi1['estacao'] == estacao)]
        x = [datetime.strptime(d, '%d/%m/%Y %H:%M') for d in arqi.datahora]
        arqi['data_hora'] = x
        arqi = arqi.reset_index(drop=True)

        datainicio=(datainicio.strftime('%Y/%m/%d %H:%M:%S'))
        arqi = arqi.loc[(arqi['data_hora'] >= datainicio)]
        arqi = arqi.reset_index(drop=True)
        df=arqi
        #first_column = df.pop('data_hora')

        # insert column using insert(position,column_name,
        # first_column) function
        #df.insert(0, 'Data_hora', first_column)


        #df.drop(columns=[ "metar", "speci", "u", "v", "gust"],inplace=True)
        df['period']=df['data_hora'].dt.hour

        df.drop(columns=["metar", "speci", "u", "v", "gust", "dewp"], inplace=True)
       # df = df.reset_index(drop=True)
        df.sort_values(by=['data_hora'], inplace=True)
        df = df.reset_index(drop=True)
        return df
    def graficos(datainicio,datafim):
        figa = make_subplots(rows=6, cols=1,
                             shared_xaxes=False,
                             vertical_spacing=0.09,
                             subplot_titles=(
                             "Intensidade do vento", " Média direção do vento", "Temperatura do ar",
                             'Media altura nuvens baixas', "Quantidade de nuvens", "Altura da base das nuvens(ft)"),

                             # column_widths=[0.7, 0.3],
                             specs= [ [{"type": "scatter"}],
                                    [{"type": "histogram"}],
                                    [{"type": "histogram"}],
                                    [{"type": "histogram"}],
                                    [{"type": "histogram"}],
                                    [{"type": "histogram"}]]
                             )

        figa.add_trace(
            go.Scatter(
                x=df["data_hora"],
                y=df["wspd"],
                mode="lines",
                name="int(kt)"

            ),
            row=1, col=1
        )

        figa.add_trace(

            go.Histogram(
                x=df["period"],
                xbins=dict(

                    size=0.5
                ),
                # y=df["altn1"],
                # mode="markers",
                name="direção do vento(graus)",
                opacity=0.75,
                y=df["wdir"],
                # y=np.mod((np.arctan2(df["u"], df["v"]) * 180/np.pi) + 180, 360),
                histfunc='avg'

            ),
            row=2, col=1
        )
        figa.add_trace(

            go.Histogram(
                x=df["period"],
                xbins=dict(

                    size=0.5
                ),
                # y=df["altn1"],
                # mode="markers",
                name="temp do ar",
                opacity=0.75,
                y=df["dryt"],
                histfunc='avg'

            ),
            row=3, col=1
        )
        figa.add_trace(

            go.Histogram(
                x=df["period"],
                xbins=dict(

                    size=0.5
                ),
                # y=df["altn1"],
                # mode="markers",
                name="altura base nuvem(ft)",
                opacity=0.75,
                y=df["altn1"],
                histfunc='avg'

            ),
            row=4, col=1
        )

        # fig.add_trace(go.Histogram(
        #     x=df["wdir"],
        #     #y=df["wspd"],
        #
        #     name='dir/média(int) vento',
        #     marker_color='#330C73',
        #     xbins=dict(
        #
        #         size=0.5
        #     ),
        #
        #     opacity=0.75,
        #     y=df["wspd"],
        #     histfunc='avg'
        # ),
        #     row=4, col=1
        # )

        figa.add_trace(go.Histogram2dContour(x=df["period"],
                                             y=df["qn1"],
                                             showscale=False,
                                             colorbar=dict(
                                                 title='Quantidade',
                                                 tickfont={'color': '#E90'},
                                                 titlefont={"color": '#FF0000'},
                                             ),
                                             contours=dict(
                                                 showlabels=True,
                                                 labelfont=dict(
                                                     family='Raleway',
                                                     color='white'
                                                 )

                                             )),

                       row=5, col=1
                       )
        figa.add_trace(go.Histogram2dContour(x=df["period"],
                                             y=df["altn1"],
                                             showscale=False,
                                             colorbar=dict(
                                                 title='Altura(ft)',
                                                 tickfont={'color': '#E90'},
                                                 titlefont={"color": '#FF0000'},
                                             ),
                                             contours=dict(
                                                 showlabels=True,
                                                 labelfont=dict(
                                                     family='Raleway',
                                                     color='white'
                                                 )

                                             )),

                       row=6, col=1
                       )


        figa.update_xaxes(title_text="datahora", row=1, col=1)
        figa.update_xaxes(title_text="hora", row=2, col=1)
        figa.update_xaxes(title_text="hora", row=3, col=1)
        figa.update_xaxes(title_text="hora", row=4, col=1)
        figa.update_xaxes(title_text="hora", row=5, col=1)
        figa.update_xaxes(title_text="hora", row=6, col=1)

        # Update yaxis properties

        figa.update_yaxes(title_text="int vento(kt)", row=1, col=1)
        figa.update_yaxes(title_text="média dir vento(graus)", row=2, col=1)
        figa.update_yaxes(title_text="média tar(graus C)", showgrid=False, row=3, col=1)
        figa.update_yaxes(title_text="média altura nuvens baixas(ft)", row=4, col=1)
        figa.update_yaxes(title_text="quantidade nuvens", row=5, col=1)
        figa.update_yaxes(title_text="altura nuvens baixas(ft)", row=6, col=1)

        aux = len(df)
        figa.update_layout(
            height=3000,
            showlegend=False,
            title_text=df.estacao[0] + ' - ' + str(datainicio),
            # + ' - ' + df.datahora[0][11:16] + ' a ' + df.datahora[aux - 1][
            # 11:16] + 'UTC',
            bargap=0.5,  # gap between bars of adjacent location coordinates
            bargroupgap=0.3  # gap between bars of the same location coordinates
        )
        return figa

    # Your streamlit code
    st.set_page_config(
        page_title="Dados Estatísticos",
        page_icon="✅",
        layout="wide",
     )
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    barra_lateral = st.sidebar.empty()
    area_seleciona = st.sidebar.selectbox("Seleciona a área:", area)
    if area_seleciona == 'Área 1':
        areasel = area_1
    else:
        areasel = area_2
    estacao_seleciona = st.sidebar.selectbox("Seleciona o Aeródromo", areasel)


    to_data = st.sidebar.date_input('Inicio:', start_date)
    from_data = st.sidebar.date_input('Fim:', end_date)
    intervalo_seleciona=st.sidebar.selectbox("Selecione o intervalo",intervalo)
    carregar_dados=st.sidebar.checkbox("Mostrar dados")

    grafico_line = st.empty()
   # grafico_candle = st.empty()

    # elementos centrais da página
    #st.title('Dados Estatísticos')



    if from_data < to_data:
        st.sidebar.error('Data de ínicio maior do que data final')
    else:
        df = consulta_dado_grafico(areasel, estacao_seleciona, to_data, from_data, area_seleciona)
        if carregar_dados:
            st.subheader('Dados')
            dados = st.dataframe(df)
            stock_select = st.sidebar.selectbox
        figura=graficos(to_data,from_data)
        grafico_line = st.plotly_chart(figura)


if __name__ == '__main__':
    if streamlit._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
