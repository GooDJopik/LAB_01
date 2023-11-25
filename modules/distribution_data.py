import csv
import datetime
import os

import modules.add_functions as ef



def distribution_date_and_data(directory_path: str) -> None:
    path = os.getcwd()
    os.chdir(directory_path)
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    with open('X.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([map(int, i[0].split("-")) for i in data])
    with open('Y.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([i[1:] for i in data])
    os.chdir(path)


def distribution_by_year(directory_path: str) -> None:
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    year_list = []
    for day in data:
        year_list.append(int(day[0].split("-")[0]))
    year_list = sorted(list(set(year_list)))
    a = 0
    b = 0
    for year in year_list:
        data_year = []
        for day in data:
            if year == int(day[0].split("-")[0]):
                data_year.append(day)
        a = "".join(data_year[0][0].split("-"))
        b = "".join(data_year[len(data_year) - 1][0].split("-"))
        with open(f"{a}_{b}.csv", 'w', encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data_year)
    os.chdir(path)

def distribution_by_week(input_file, directory_path) -> None:
    data = ef.read_data(r"D:\Python_lab\python_lab\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    data = ef.read_csv(input_file)
    data['date'] = ef.datetime(data['date'])
    
    for week_start in data['date'].dt.to_period('W').unique():
        week_end = week_start.end_time
        week_data = data[(data['date'] >= week_start.start_time) & (data['date'] <= week_end)]
        output_file = f'{directory_path}/{week_data.iloc[0]["date"].strftime("%Y%m%d")}_{week_data.iloc[-1]["date"].strftime("%Y%m%d")}.csv'
        week_data.to_csv(output_file, index=False)
    os.chdir(path)
