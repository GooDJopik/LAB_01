
from bs4 import BeautifulSoup
import requests
import csv
import os

import modules.add_functions as ef

def correct_wind_info(wind: str) -> tuple:
    durection, speed = wind.split()
    return durection, speed[:len(speed)-3]

def parser(year_from:int, year_to:int, step=1) -> list:
    parser_data = []
    for year in range(year_from, year_to + 1, step):
        for month in range(1, 13):
            URL = f"https://www.gismeteo.ru/diary/4618/{year}/{month}/"
            html_page = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
            soup = BeautifulSoup(html_page.text, 'html.parser')
            for day in soup.find_all('td', class_="first"):
                try:
                    temp = day.find_next()
                    press = temp.find_next()
                    wind = press.find_next_sibling().find_next_sibling().find_next_sibling()
                    durection, digit_speed = correct_wind_info(wind.text)
                    parser_data.append([str(year) + "-" + str(month).zfill(2) + "-" + day.text.zfill(2), int(temp.text), press.text, durection, digit_speed])
                except:
                    pass
    return parser_data   


@ef.change_work_dir(name=r"\datasets")
         
def upload_csv(parser_data: list) -> None:
    with open('dataset.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(parser_data)


'''upload_csv(parser(2008, 2023))'''






