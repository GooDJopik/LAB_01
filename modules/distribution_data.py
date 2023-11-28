import csv
import datetime
import os
import pandas as pd

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
    data['date'] = pd.to_datetime(data['date'])
    
    for year in data['date'].dt.year.unique():
        year_data = data[data['date'].dt.year == year]
        output_file = f'{directory_path}/{year_data.iloc[0]["date"].strftime("%Y%m%d")}_{year_data.iloc[-1]["date"].strftime("%Y%m%d")}.csv'
        year_data = csv.writer(output_file, index=False)
    os.chdir(path)

def distribution_by_week(directory_path: str) -> None:
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    data['date'] = datetime(data['date'])
    
    for week_start in data['date']:
        week_end = week_start.end_time
        week_data = data[(data['date'] >= week_start.start_time) & (data['date'] <= week_end)]
        output_file = f'{directory_path}/{week_data.iloc[0]["date"].datetime.strptime("%Y%m%d")}_{week_data.iloc[-1]["date"].strftime("%Y%m%d")}.csv'
        week_data = csv.writer(output_file, index=False)
    os.chdir(path)


