import requests
import pandas as pd
import streamlit as st
import baixarmodeloNovoprojeto
import baixaamodeloNovometeograma

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

    extracted_data = []
    for i in range(len(weather_data)):
        date, time = (weather_data['datazulu'][i]).strftime('%d/%m/%Y %H:%M').split(' ')
        #date, time = weather_data.datazulu[i].split(' ')

        temp = weather_data['tar'][i]
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


    link,data,horazulu=baixarmodeloNovoprojeto.Scraper(city)
   # city='SBJR'
   # link='https://www.windy.com/-22.910/-43.163/meteogram?-22.935,-43.163,13,m:c0YaeXe'
   # horazulu=3
    print('chegou aqui 333333333')
    data1=baixaamodeloNovometeograma.Scraper(city,link,horazulu)
    print('chegou aqui 2222222222222')
   

    #except Exception as e:
    #    st.error(f"Could not get the data because {e}. Exiting...")
    #    st.stop()
    #data = pd.read_csv("dadosecmwf_area2_1104.csv")
    data=pd.merge(data, data1, how='inner', on='datahora')
    print('chegou aqui 44444444444444')
    data=data.drop(['tar_y', 'estacao_y', 'datazulu_y'], 1)
    print('chegou aqui 5555555555555')
    data=data.rename(columns={'estacao_x': 'estacao', 'tar_x': 'tar', 'datazulu_x': 'datazulu'})
    print('chegou aqui 66666666666666')


    return data

