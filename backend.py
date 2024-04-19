import numpy as np
import requests
import pandas as pd
import streamlit as st


def lookup_coord(city_name,usu):
    """Function to lookup the names of city"""
    if usu==1:
        df = pd.read_csv("cities_transformed3.csv")
    else:
        df = pd.read_csv("cities_transformed2.csv")
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
    for i in range(len(weather_data['list'])):
        date, time = weather_data['list'][i]['dt_txt'].split(' ')
        act_temp = weather_data['list'][i]['main']['temp']
        feel_temp = weather_data['list'][i]['main']['feels_like']
        min_temp = weather_data['list'][i]['main']['temp_min']
        max_temp = weather_data['list'][i]['main']['temp_max']
        pressure = weather_data['list'][i]['main']['pressure']
        sea_level = weather_data['list'][i]['main']['sea_level']
        grnd_level = weather_data['list'][i]['main']['grnd_level']
        humidity = weather_data['list'][i]['main']['humidity']
        wspd=weather_data['list'][i]['wind']['speed']*2
        wdir=weather_data['list'][i]['wind']['deg']
        gust=weather_data['list'][i]['wind']['gust']*2
        if 'visibility' in weather_data['list'][i]:
            visibilidade=str(weather_data['list'][i]['visibility'])
        else:
            visibilidade = 'Nan'
        #chuva=weather_data['list'][i]['rain']['3h']
        weather_status = weather_data['list'][i]['weather'][0]['main']
        extracted_data.append(
            (weather_data['city']['name'], weather_data['city']['country'], date, time, act_temp, feel_temp,
             min_temp, max_temp, pressure, sea_level, grnd_level, humidity, weather_status,wspd,wdir,gust,visibilidade))

    # push_data(extracted_data)
    return extracted_data


def authenticate(lat, lon):
    """Function to request information from OpenWeatherMap API giving the necessary details"""
    try:

        API_KEY = '6735133fcb33d07e90beaff802fde5a0'
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&lang=pt_br&appid={API_KEY}")
        if not response.status_code == 200:
            st.error("Failed to get data. Reason: ", response.json()['message'])
            exit()
    except Exception as e:
        #st.error(f"Could not get the data because {e}. Exiting...")
        #st.stop()
        continue
    data = response.j
    son()

    return data

