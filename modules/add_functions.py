import os
import csv


def read_data(path: str) -> list:
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in csv.reader(file):
            data.append(line)
    return data


def change_work_dir(name: str):
    def decorator(func):
        def wrapper():
            path = os.getcwd()
            os.chdir(f"{path}{name}")
            func()
            os.chdir(path)
        return wrapper
    return decorator


def growth(next_day: int, today: int) -> int:
    if next_day < today:
        return (next_day + 31) - today
    return next_day - today