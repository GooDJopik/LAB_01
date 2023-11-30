import datetime
import os

import modules.distribution_data as ef


def search(path: str, date: datetime) -> list | None:
    for day in ef.read_data(path):
        if day[0] == str(date):
            return day[1:]
  
  
def find(path: str, date: datetime) -> list | None:
    data = ef.read_data(path)
    for i in range(len(data)):
        if data[i][0] == str(date):
            return i


def search_by_year(date: datetime) -> list | None:
    directory = "datasets/data_by_year"
    for filename in os.listdir(directory):
        if (int(filename[0:4]) == date.year):
            data = ef.read_data(f"{directory}/{filename}")
            for day in data:
                if day[0] == str(date):
                    return day[1:]


def search_by_week(date: datetime) -> list | None:
    directory = "datasets/data_by_week"
    for filename in os.listdir(directory):
        left_date = datetime.datetime.strptime(filename[:8], '%Y%m%d').date()
        right_date = datetime.datetime.strptime(
            filename[9:17], '%Y%m%d').date()
        if (left_date <= date <= right_date):
            data = ef.read_data(f"{directory}/{filename}")
            for day in data:
                if day[0] == str(date):
                    return day[1:]


def search_by_date(date: datetime) -> list | None:
    data_from_x = ef.read_data(f"datasets/date_and_data/X.csv")
    for row, value in enumerate(data_from_x):
        time = "-".join(value)
        if time == str(date):
            data_from_y = ef.read_data(f"datasets/date_and_data/Y.csv")
            return data_from_y[row]