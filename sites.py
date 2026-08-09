import streamlit as st
import sys
from datetime import datetime, timedelta
from streamlit import runtime
from streamlit.web import cli as stcli
from streamlit_toggle import toggle
import numpy as np

def main():
    import requests
    import streamlit as st
    from datetime import datetime, timedelta,timezone
    import pandas as pd
    global selusuario

    def get_coordinates(city_name):
        url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
        headers = {"User-Agent": "WeatherDashboardApp/1.0 (edomenico813@gmail.com)"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            location_data = response.json()
            if location_data:
                location = location_data[0]
                return float(location['lat']), float(location['lon'])
            else:
                st.warning("City not found. Try adding the country name (e.g., 'Paris, France').")
                return None, None
        else:
            st.error(f"API request failed with status code {response.status_code}: {response.text}")
            return None, None

    def get_weather_data(lat, lon, hours):

        if selusuario == "Previsor CMA-1GL":

            #url = f"https://api.open-meteo.com/v1/forecast?latitude={lat[0]}&longitude={lon[0]}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m,visibility,cloud_cover_low,precipitation,weather_code&forecast_days=4"
            #url = f"https://api.open-meteo.com/v1/forecast?latitude={lat[0]}&longitude={lon[0]}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m,visibility,cloud_cover_low,precipitation,weather_code&models=best_match&forecast_days=4"
            url = f"https://ensemble-api.open-meteo.com/v1/forecast?latitude=-22&longitude=-43&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m,visibility,cloud_cover_low,precipitation,weather_code&forecast_days=4"
        else:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m,visibility,cloud_cover_low,precipitation,weather_code&forecast_days=4"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to retrieve weather data.")
            return None
    def temperatura(df):
        from datetime import datetime
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
      # import numpy as np
        ##"""Container for temperature time series"""
        # vento_df = pd.DataFrame(
        #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})

        fig = px.scatter(title='Temperatura')
        fig.add_scatter(x=df['Time'], y=df["Temperature (°C)"], name='Temperatura (°C)')
        #fig.add_scatter(x=df['data_hora'], y=df['wdir'], name='Dir.vento(graus)')
        fig.update_yaxes(title="Temperatura(°C)")
        fig.update_xaxes(title="Data")
        st.plotly_chart(fig, use_container_width=True)
        return

    def visibilidade(df):
        from datetime import datetime
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
      # import numpy as np
        ##"""Container for temperature time series"""
        # vento_df = pd.DataFrame(
        #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})

        fig = px.scatter(title='Visibilidade')
        fig.add_scatter(x=df['Time'], y=df["visibility"], name='Visibilidade(m)')
        #fig.add_scatter(x=df['data_hora'], y=df['wdir'], name='Dir.vento(graus)')
        fig.update_yaxes(title="Visibilidade(m)")
        fig.update_xaxes(title="Data")
        st.plotly_chart(fig, use_container_width=True)
        return
    def nuvembaixa(df):
        from datetime import datetime
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
      # import numpy as np
        ##"""Container for temperature time series"""
        # vento_df = pd.DataFrame(
        #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})

        fig = px.scatter(title='Cobertura de nuvem baixa')
        fig.add_scatter(x=df['Time'], y=df["cloud_cover_low"], name='Nuvem baixa')
        #fig.add_scatter(x=df['data_hora'], y=df['wdir'], name='Dir.vento(graus)')
        fig.update_yaxes(title="Nuvem baixa")
        fig.update_xaxes(title="Data")
        st.plotly_chart(fig, use_container_width=True)
        return

    def precipitacao(df):
        from datetime import datetime
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
      # import numpy as np
        ##"""Container for temperature time series"""
        # vento_df = pd.DataFrame(
        #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})

        fig = px.scatter(title='Precipitação(mm)')
        fig.add_scatter(x=df['Time'], y=df["precipitation"], name='Precipitação(mm)')
        #fig.add_scatter(x=df['data_hora'], y=df['wdir'], name='Dir.vento(graus)')
        fig.update_yaxes(title="Precipitação(mm)")
        fig.update_xaxes(title="Data")
        st.plotly_chart(fig, use_container_width=True)
        return

    def vento(df):
        from datetime import datetime
        import plotly
        import plotly.express as px
        import plotly.graph_objects as go
        from plotly.subplots import make_subplots
      # import numpy as np
        ##"""Container for temperature time series"""
        # vento_df = pd.DataFrame(
        #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})

        fig = px.scatter(title='Vento')
        fig.add_scatter(x=df['Time'], y=df["Wind Speed (kt)"], name='Intensidade(kt)')
        fig.add_scatter(x=df['Time'], y=df['Wind Direction (°)'], name='Dir.vento(graus)')
        fig.update_yaxes(title="Valor")
        fig.update_xaxes(title="Data")
        st.plotly_chart(fig, use_container_width=True)
        return

    def obter_lat_lon(nomedaestacao,noarea,areaselecionada):
        df = pd.read_csv("estacaomodelos.csv")

        df1=df[df['estacao'] ==nomedaestacao]
        lat1=df1['lat']
        lon1 = df1['lon']

        return lat1.values,lon1.values

    def principal(lat,lon):

        #city_name = st.text_input("Nome da Cidade", value="cabo frio")

            forecast_duration = st.slider("Selecione a duração da previsão(horas)", min_value=12, max_value=48,
                                          value=96, step=12)

            #lat, lon = get_coordinates(city_name)
            if lat and lon:
                data = get_weather_data(lat, lon, forecast_duration)
                if data:
                    # times = [datetime.now() + timedelta(hours=i) for i in range(forecast_duration)]
                    times = [datetime.combine(datetime.today().date(), datetime.min.time()) + timedelta(hours=i) for i
                             in
                             range(forecast_duration)]
                    df = pd.DataFrame({"Time": times})
                    df["Temperature (°C)"] = data['hourly']['temperature_2m'][:forecast_duration]
                    df["Humidity (%)"] = data['hourly']['relative_humidity_2m'][:forecast_duration]
                    df["Wind Speed (m/s)"] = data['hourly']['wind_speed_10m'][:forecast_duration]
                    df["Wind Speed (kt)"] = df["Wind Speed (m/s)"] * 0.539957
                    df["Wind Speed (kt)"] = df["Wind Speed (kt)"].astype(int)
                    df["Wind Direction (°)"] = data['hourly']['wind_direction_10m'][:forecast_duration]
                    df["visibility"] = data['hourly']['visibility'][:forecast_duration]
                    df["cloud_cover_low"] = data['hourly']['cloud_cover_low'][:forecast_duration]
                    df["precipitation"] = data['hourly']['precipitation'][:forecast_duration]
                    df["codigo"] = data['hourly']['weather_code'][:forecast_duration]

                    # if st.button("Get Weather Data"):
                    #     lat, lon = get_coordinates(city_name)
                    #     if lat and lon:
                    #         data = get_weather_data(lat, lon, forecast_duration)
                    #         if data:
                    #             #times = [datetime.now() + timedelta(hours=i) for i in range(forecast_duration)]
                    #             times = [datetime.combine(datetime.today().date(), datetime.min.time()) + timedelta(hours=i) for i in range(forecast_duration)]
                    #             df = pd.DataFrame({"Time": times})
                    #
                    #             if "Temperature (°C)" in parameter_options:
                    #                 df["Temperature (°C)"] = data['hourly']['temperature_2m'][:forecast_duration]
                    #                 st.subheader(f"Temperatura prevista")
                    #                 st.line_chart(df.set_index("Time")["Temperature (°C)"])
                    #
                    #             if "Humidity (%)" in parameter_options:
                    #                 df["Humidity (%)"] = data['hourly']['relative_humidity_2m'][:forecast_duration]
                    #                 st.subheader(f"Umidade prevista")
                    #                 st.line_chart(df.set_index("Time")["Humidity (%)"])
                    #
                    #             if "Wind Speed (m/s)" in parameter_options:
                    #                 df["Wind Speed (m/s)"] = data['hourly']['wind_speed_10m'][:forecast_duration]
                    #                 df["Wind Speed (kt)"] = df["Wind Speed (m/s)"]*0.539957
                    #                 df["Wind Speed (kt)"]=df["Wind Speed (kt)"].astype(int)
                    #                 st.subheader(f"Intensidade do vento")
                    #                 st.line_chart(df.set_index("Time")["Wind Speed (kt)"])
                    #             if "Wind Direction (°)" in parameter_options:
                    #                 df["Wind Direction (°)"] = data['hourly']['wind_direction_10m'][:forecast_duration]
                    #
                    #                 st.subheader(f"Direção do vento")
                    #                 st.line_chart(df.set_index("Time")["Wind Direction (°)"])
                    # st.subheader("Current Weather Summary")
                    # #col1, col2, col3,col4 = st.columns(4)

                    temperatura(df)
                    vento(df)
                    visibilidade(df)
                    nuvembaixa(df)
                    precipitacao(df)
                    with st.expander(label="Mostrar dados:"):
                        df2=df
                        df2.drop('Wind Speed (m/s)', inplace=True, axis=1)
                        df2.rename(columns={'Temperature (°C)': 'dryt'}, inplace=True)
                        df2.rename(columns={'Humidity (%)': 'relh'}, inplace=True)
                        df2.rename(columns={'Wind Speed (kt)': 'wspd'}, inplace=True)
                        df2.rename(columns={'Wind Direction (°)': 'wdir'}, inplace=True)
                        df2.rename(columns={'visibility': 'visi'}, inplace=True)
                        df2.rename(columns={'cloud_cover_low': 'nuvb'}, inplace=True)
                        df2.rename(columns={'precipitation': 'prp'}, inplace=True)

                        st.table(df2)

    # datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)
    # col1.metric("🌡️ Temperature(°)", df.loc[df['Time'] ==datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0).strftime("%d/%m/%Y %H:%M:%S"),'Temperature (°C)'].iloc[0])
    # df.loc[df['Time'] == datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0).strftime(
    #    "%d/%m/%Y %H:%M:%S"), 'wind_speed_10m]'.iloc[0])
    # col2.metric("💧 Humidity(%)", df.loc[df['Time'] == datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0).strftime(
    #    "%d/%m/%Y %H:%M:%S"), 'Humidity (%)'].iloc[0])
    # col3.metric("🌬️ Wind Speed(kt)", df.loc[df['Time'] == datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0).strftime(
    #   "%d/%m/%Y %H:%M:%S"), 'Wind Speed (kt)'].iloc[0])
    # col4.metric("🌬️ Wind Direction (°))",
    #           df.loc[df['Time'] == datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0).strftime(
    #               "%d/%m/%Y %H:%M:%S"), 'Wind Direction (°)'].iloc[0])

    # Executar a página selecionada
    st.title("Previsão Numérica🌤️")
    st.write("Fonte:  Open-Meteo combina os resultados de modelos de vários serviços meteorológicos")
    
        
    area = ['Área 1', 'Área 2']

    area_1 = ['SBJR', 'SBMI', 'SBES', 'SBME', 'SBFS', 'SBCP', 'SBRJ', 'SBCB', 'SBVT', 'SBPS', 'SBGL', 'SBNT', 'SBMS',
              'SBAC','SBJE','SBPB', 'SBAR', 'SBMO', 'SBRF', 'SBJP', 'SBSG', 'SBFZ', 'SBSL', 'SBTE', 'SBJU', 'SBKG', 'SNRU', 'SBFN',
              'SBPL','SBPJ']
    area_2 = ['SBRD', 'SBVH','SBJI', 'SSKW', 'SBRB', 'SWEI', 'SBCY', 'SBPV', 'SBCZ', 'SBTT', 'SBIZ', 'SWGN', 'SBMA',
              'SBCJ', 'SBHT','SBTB', 'SBOI', 'SBBE', 'SBMQ', 'SBSN', 'SBSO', 'SBSI', 'SBAT', 'SBIH', 'SWPI', 'SBMY', 'SBTF', 'SBUY',
              'SBUA', 'SBEG','SBBV']
    while True:
        with st.sidebar:
            st.write('Escolha as opções para visualizar')
            with st.container(border=True):
                # st.divider()
                selusuario=st.radio("Escolha o usuário", ["Previsor CMA-1GL", "Público Geral"], horizontal=True)

                if selusuario=="Previsor CMA-1GL":
                    selarea = st.radio("Escolha a área", ["Área 1", "Área 2"], horizontal=True)
                    #ong = st.toggle('Obter Dados')
                    st.divider()
                    if selarea == "Área 1":
                        # with col1:
                        # st.header('Área 1')
                        nomedaestacao = st.radio("Área 1",area_1)
                        noarea = 1
                        areaselecionada=area_1
                    else:
                        # st.header('Área 2')
                        nomedaestacao = st.radio("Área 2",area_2)
                        noarea = 2
                        areaselecionada = area_2
                else:
                    city_name = st.text_input("Nome da Cidade", value="cabo frio")
                    if st.button("Ok"):

                        lat, lon = get_coordinates(city_name)
                    else:
                        lat, lon = get_coordinates(city_name)


                st.markdown(
                    """
            
                    e-mail: edomenico813@gmail.com
                
                
                    """
                )
        with st.spinner('Loading...'):
            if selusuario == "Previsor CMA-1GL":
                lat, lon = obter_lat_lon(nomedaestacao, noarea, areaselecionada)
            principal(lat, lon)
        break
    #if selusuario=="Previsor CMA-1GL":
     #   st.write("Lat",lat)
     #   st.write("Lon",lon)
    #else:
    #    st.write("Lat",lat)
    #    st.write("Lon",lon)


main()
    

    
