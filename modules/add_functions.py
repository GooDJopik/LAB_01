
import csv



def read_data(path: str) -> list:
    data = []
    with open(path, "r", encoding="utf-8") as file:
        for line in csv.reader(file):
            data.append(line)
    return data
