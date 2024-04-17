import numpy as np

import backend2
import baixarmodeloNovoprojeto
from streamlit import runtime
import sys
from streamlit.web import cli as stcli
import streamlit as st
import pandas as pd
import plotly.express as px


def search2(city,usu):
    try:
        lat, lon = backend2.lookup_coord(city,usu)
            # st.write(lat)
        print('novo_projeto 1')
        data = backend2.authenticate(city)
            # st.write(data)
        print('novo_projeto 2')
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








