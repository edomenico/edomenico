import numpy as np

import backend2
#import baixarmodeloNovoprojeto
from streamlit import runtime
import sys
from streamlit.web import cli as stcli
import streamlit as st
import pandas as pd
import plotly.express as px

def lookup_coord(city_name,usu):
    """Function to lookup the names of city"""
    print('chegou aqui')
    if usu==1:
        df = pd.read_csv("cities_transformed3.csv")
    else:
        df = pd.read_csv("cities_transformed3.csv")
    city_data = df[df['city'].str.lower() == city_name]
    if not city_data.empty:

        lat = city_data['lat'].iloc[0]
        lon = city_data['lon'].iloc[0]
        return lat, lon
    else:
        return None


def sort_data(weather_data):
    """"Function to extract data from json"""
    print('extracted')
    print(weather_data)
    

    extracted_data = []
    for i in range(len(weather_data)):
        date, time = (weather_data['datazulu'][i]).strftime('%d/%m/%Y %H:%M').split(' ')
        #date, time = weather_data.datazulu[i].split(' ')

        temp = weather_data['tar'][i]
        print(temp)
        #feel_temp = weather_data['list'][i]['main']['feels_like']
        #min_temp = weather_data['list'][i]['main']['temp_min']
        #max_temp = weather_data['list'][i]['main']['temp_max']
        #pressure = weather_data['list'][i]['main']['pressure']
        #sea_level = weather_data['list'][i]['main']['sea_level']
        #grnd_level = weather_data['list'][i]['main']['grnd_level']
        #humidity = weather_data['list'][i]['main']['humidity']
        wspd=weather_data['wspd'][i]
        wdir=weather_data['wdir'][i]
        gust=weather_data['gust'][i]
        visibilidade=weather_data['vis'][i]
        if visibilidade=='9999':
            visibilidade='10000'

        chuva=weather_data['prp'][i]
        td=(weather_data['tdr'][i])
        ur= str(round(100 - 5 * (int(temp) - int(td))))
        nbaixas=str(weather_data['nbaixa'][i])
        if nbaixas[-1]=='k':
            nbaixas=str(int(nbaixas[0:len(nbaixas)-1])*3281)
        elif nbaixas=='--':
            nbaixas = 'Nil'
        else:
            nbaixas=str(int(int((nbaixas))*3.281))
        if len(nbaixas)>5:
            nbaixas=nbaixas[0:5]

        tp=weather_data['tp'][i]
        if tp=='':
            tp='Nil'
        cld=weather_data['cld'][i]
        cldcb=weather_data['cldcb'][i]
        pressao=(weather_data['pressao'][i])
        #weather_status = weather_data['list'][i]['weather'][0]['main']
        extracted_data.append(
            (weather_data['estacao'][i], date, time, temp,ur,pressao,
             tp, cld, cldcb,wspd,wdir,gust,visibilidade,nbaixas))

    # push_data(extracted_data)
    return extracted_data


def authenticate(city):

    """Function to request information from OpenWeatherMap API giving the necessary details"""
    #try:

    print('chegou aqui 2')


    link,data1,horazulu=baixarmodeloNovoprojeto.Scraper(city)
   # city='SBJR'
   # link='https://www.windy.com/-22.910/-43.163/meteogram?-22.935,-43.163,13,m:c0YaeXe'
   # horazulu=3
    print('chegou aqui 333333333')
    print (data1)
    data2=baixaamodeloNovometeograma.Scraper(city,link,horazulu)
    print('chegou aqui 2222222222222')
   

    #except Exception as e:
    #    st.error(f"Could not get the data because {e}. Exiting...")
    #    st.stop()
    #data = pd.read_csv("dadosecmwf_area2_1104.csv")
    data3=pd.merge(data1, data2, how='inner', on='datahora')
    print(data3)
    print('chegou aqui 44444444444444')
    #data1=data.drop(['tar_y', 'estacao_y', 'datazulu_y'], axis=1)
    print('chegou aqui 5555555555555')
    
    data4=data3.rename(columns={'estacao_x': 'estacao', 'tar_x': 'tar', 'datazulu_x': 'datazulu'})
    print('chegou aqui 66666666666666')
    print(data4)


    return data4

def search2(city,usu):
    try:
        lat, lon = backend2.lookup_coord(city,usu)
            # st.write(lat)
        print('novo_projeto 1')
        data = backend2.authenticate(city)
            # st.write(data)
        print('novo_projeto 2')
        print(data)
        extracted_data = backend2.sort_data(data)
            # st.write(extracted_data)
        return extracted_data, lat, lon
    except Exception as e:
        print(f"Cannot locate this city. Reason: {e}")




def temp_time_series2(df):
    """Container for temperature time series"""
    temp_time_df = pd.DataFrame(
        {'temp': df['temp'], 'ur': df['ur'],'timestamp': df['timestamp']})
    fig = px.line(temp_time_df, x='timestamp', y=['temp', 'ur'],
                  title='Temperatura(°C) e Umidade Relativa(%)')
    fig.update_yaxes(title="Valor")
        #fig.update_xaxes(title="dia")
    new = {'temp': 'Temperatura Atual(°C)', 'ur': 'Umidade (%)'}
    fig.for_each_trace(lambda t: t.update(name=new[t.name]))
        # fig.update_legends(selector={'actual_temp': 'Air Temperature'})
        # fig = px.scatter(title='Temp')
        # fig.add_scatter(x=df['timestamp'], y=df['actual_temp'],mode='lines',name='Actual Temperature')
        # fig.add_scatter(x=df['timestamp'], y=df['feels_like_temp'],mode='lines',name='Feels-like Temperature')
        # fig.update_xaxes(title="Date", tickformat="%d-%m-%Y")
        # fig.update_yaxes(title="Temperature (°C)", range=[df['min_temp'].min(), df['max_temp'].max()])
    st.plotly_chart(fig, use_container_width=True)


def weather_pie(df):
    """Container for pie chart of weather conditions"""
    labels = list(set(df['tp']))
    values = [sum([i == j for i in df['tp']]) for j in labels]
    fig = px.pie(values=values, labels=labels, title="Condições do tempo", hover_name=labels, names=labels)
    st.plotly_chart(fig, use_container_width=True)


def min_max2(df):
    """Container for minimum and maximum temperatures"""
        # min_max_df = pd.DataFrame({'max_temp': df.groupby('date')['max_temp'].max(), 'date': df['date'].unique(), 'min_temp':df.groupby('date')['min_temp'].min()})
        # fig = px.line(min_max_df, x= 'date', y=['max_temp','min_temp'],title='Minimum and Maximum Temperature')
        # new = {'max_temp':'Maximum Temperature', 'min_temp': 'Minimum Temperature'}
        # fig.for_each_trace(lambda t: t.update(name = new[t.name]))
    ####df['data'].unique()[0:len(df['data'].unique()) - 1]
    #####df.groupby('data')['temp'].max()[0:len(df['data'].unique()) - 1]
    fig = px.scatter(title='Temperatura máxima e mínima')
    fig.add_scatter(x=df['data'].unique()[0:len(df['data'].unique()) - 1], y=df.groupby('data')['temp'].max()[0:len(df['data'].unique()) - 1], name='Temperatura Máxima')
    fig.add_scatter(x=df['data'].unique()[0:len(df['data'].unique()) - 1], y=df.groupby('data')['temp'].min()[0:len(df['data'].unique()) - 1], name='Temperatura Mínima')
    fig.update_yaxes(title="Temperatura (°C)")
    st.plotly_chart(fig, use_container_width=True)


def vento2(df):
    """Container for temperature time series"""
        # vento_df = pd.DataFrame(
        #     {'dir.vento': df['dir vento'], 'int.vento': df['int vento'], 'timestamp': df['timestamp']})

    fig = px.scatter(title='Vento')
    fig.add_scatter(x=df['timestamp'], y=df['int vento'], name='Int.vento(kt)')
    fig.add_scatter(x=df['timestamp'], y=df['dir vento'], name='Dir.vento(graus)')
    fig.update_yaxes(title="Valor")
    st.plotly_chart(fig, use_container_width=True)








