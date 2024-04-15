import backend

from streamlit import runtime
import sys
from streamlit.web import cli as stcli
import streamlit as st
import pandas as pd
import plotly.express as px
import novo_projeto2
def main():


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
            
            result, lat, lon = novo_projeto2.search2(city, usu)
            # st.write(result)
            df = pd.DataFrame(result)
            df.rename(
                columns={0: 'estacao', 1: 'data', 2: 'hora', 3: 'temp', 4: 'ur', 5: 'pressao', 6: 'tp',
                         7: 'ceu',8: 'ncb',9: 'int vento',
                         10: 'dir vento', 11: 'raj vento', 12: 'visibilidade', 13: 'nbaixas'}, inplace=True)




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
                        novo_projeto2.temp_time_series2(df)
                    with col2:
                        novo_projeto2.weather_pie(df)

                    col3, col4 = st.columns((5, 5))
                    with col3:
                        novo_projeto2.min_max2(df)
                    with col4:
                        novo_projeto2.vento2(df)

                if show_map and city:
                    st.map(pd.DataFrame({'lat': [lat], 'lon': [lon]}), use_container_width=True)

                st.divider()

                with st.expander(label="Mostrar dados:"):
                    st.table(df)
st.set_page_config(page_title='Previsão', page_icon=':satellite:', layout='wide',
                       initial_sidebar_state='expanded')
st.session_state
main()
