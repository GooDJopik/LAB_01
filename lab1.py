'''
import os

import requests

URL = "https://www.gismeteo.ru/weather-samara-4618/"
html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})


import webbrowser
webbrowser.open('https://www.gismeteo.ru/diary/4618/2023/9/', new=2)
from bs4 import BeautifulSoup
import requests
import os



URL = "https://www.gismeteo.ru/diary/4618/2023/9/'"
html_page = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})

from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd


--------------------------------------
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.gismeteo.ru/weather-samara-4618/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []

# Извлечение данных о погоде для каждого дня
for day in soup.find_all('div', class_='w_daily'):
    date = day.find('div', class_='date').text.strip()
    temperature = day.find('div', class_='temperature').text.strip()
    pressure = day.find('div', class_='value m_press torr').text.strip()
    wind = day.find('div', class_='w_wind').text.strip()
    
    data.append([date, temperature, pressure, wind])

# # Создание и сохранение данных в CSV-файл
# df = pd.DataFrame(data, columns=['Дата', 'Температура', 'Давление', 'Ветер'])
# df.to_csv('dataset.csv', index=False)

'''
import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.gismeteo.ru/diary/4618/2023/9/'"
def get_weather_data(url):
    response = requests.get(URL, headers={"User-Agent":"Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    for day in soup.find_all('div', class_='w_daily'):
        date = day.find('div', class_='date').text.strip()
        # temper_after = day.find('div', class_='"first_in_group positive"').text.strip()
        # temper_eve = day.find('div', class_='temperature').text.strip()
        # temperature = (temper_after+temper_eve)//2222
        temperature = day.find('div', class_='"temperature"').text.strip()
        pressure = day.find('div', class_='value m_press torr').text.strip()
        wind = day.find('div', class_='w_wind').text.strip()

        data.append([date, temperature, pressure, wind])

    return data

def save_weather_data(data, filename):
    df = pd.DataFrame(data, columns=['Дата', 'Температура', 'Давление', 'Ветер'])
    df.to_csv(filename, index=False)
    print(f"Данные сохранены в файл '{filename}'")

def main():
    base_url = 'https://www.gismeteo.ru'
    city_code = '4618' # Код города
    start_date = '2022-01-01'  # Начальная дата
    end_date = '2022-01-31'  # Конечная дата

    # Составление URL-адреса с указанием даты
    url = f'{base_url}/weather-samara-{city_code}/{start_date}/{end_date}/'
    
    weather_data = get_weather_data(url)
    save_weather_data(weather_data, 'dataset.csv')

if __name__ == '__main__':
    main()

