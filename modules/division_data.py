import csv
import datetime
import os

import modules.add_functions as ef


@ef.change_work_dir(name=r"\datasets\date_and_data")
def division_date_and_data() -> None:
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    with open('X.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([map(int, i[0].split("-")) for i in data])
    with open('Y.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows([i[1:] for i in data])


@ef.change_work_dir(name=r"\datasets\data_by_year")
def division_by_year() -> None:
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
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


@ef.change_work_dir(name=r"\datasets\data_by_week")
def division_by_week() -> None:
    data = ef.read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    day_of_week = 6
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
            day_of_week += ef.growth(int(data[i + 1][0].split("-")[2]),
                                  int(data[i][0].split("-")[2]))
            continue
        data_week.append(data[i])
        day_of_week += ef.growth(int(data[i + 1][0].split("-")[2]),
                              int(data[i][0].split("-")[2]))
    a = "".join(data_week[0][0].split("-"))
    b = "".join(data_week[len(data_week) - 1][0].split("-"))
    with open(f"{a}_{b}.csv", 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data_week)
    

def get_data(date: datetime) -> list | None:
    for i in ef.read_data("datasets/dataset.csv"):
        if i[0] == str(date):
            return i[1:]