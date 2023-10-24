from ast import main
from bs4 import BeautifulSoup
import requests
import csv
import os

def parser(year_from, year_to, step=1):
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
                    parser_data.append([day.text + "." + str(month).zfill(2) + "." + str(year), temp.text + "°C", press.text + "mm.pt.ct.", wind.text])
                except:
                    print("Parsing error for " + day.text + "." + str(month).zfill(2) + "." + str(year))
    return parser_data   
         

def upload_csv(parser_data):
    with open('dataset.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(parser_data)


upload_csv(parser(2008, 2023))

if __name__ == '__main__':
    main()





