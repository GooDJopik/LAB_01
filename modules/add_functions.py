import os
import csv
import datetime


def read_data(path: str) -> list:
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in csv.reader(file):
            data.append(line)
    return data

def growth(today: str, next_day: str) -> int:
    current_day = datetime.datetime.strptime(today, '%Y-%m-%d').date()
    following_day = datetime.datetime.strptime(next_day, '%Y-%m-%d').date()
    return (following_day - current_day).days