import csv
import datetime
import os

import modules.add_functions as ef



def division_date_and_data(directory_path: str) -> None:
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


def division_by_year(directory_path: str) -> None:
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

def division_by_week(directory_path: str, start_day: int) -> None:
    data = ef.read_data(r"D:\Python_lab\python_lab\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    day_of_week = start_day
    data_week = [data[0]]
    for i in range(1, len(data) - 1):
        if day_of_week >= 7:
            data_week.append(data[i])
            day_of_week = 0
            a = "".join(data_week[0][0].split("-"))
            b = "".join(data_week[len(data_week) - 1][0].split("-"))
            with open(f"{a}_{b}.csv", 'w', encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data_week)
            data_week.clear()
            day_of_week += ef.growth(data[i][0], data[i+1][0])
            continue
        data_week.append(data[i])
        day_of_week += ef.growth(data[i][0], data[i+1][0])
    os.chdir(path)
