import csv
import datetime
import os

import add_functions as ef



def distribution_date_and_data(directory_path: str) -> None:
    path = os.getcwd()
    os.chdir(directory_path)
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    with open('X.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        new_data = [i[0].replace("-") for i in data]
        writer.writerows([new_data])
    with open('Y.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        new_data = [i[0] for i in data]
        writer.writerows([new_data])
    os.chdir(path)


def distribution_by_year(directory_path: str) -> None:
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    
    for year in data():
        year_data = data[data['date'] == year]
        output_file = f'{directory_path}/{year_data.iloc[0]["date"].strftime("%Y%m%d")}_{year_data.iloc[-1]["date"].strftime("%Y%m%d")}.csv'
        with open(output_file, 'w', encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(year_data)
    os.chdir(path)

def distribution_by_week(directory_path: str) -> None:
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    
    for week_start in data['date']:
        week_end = week_start
        week_data = data[(data['date'] >= week_start) & (data['date'] <= week_end)]
        output_file = f'{directory_path}/{week_data.iloc[0]["date"].strftime("%Y%m%d")}_{week_data.iloc[-1]["date"].strftime("%Y%m%d")}.csv'
    with open(output_file, 'w', encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(week_data)        
    os.chdir(path)