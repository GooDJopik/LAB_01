import csv
import os
import pandas as pd

def read_data(file_path: str) -> list:
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def distribution_date_and_data(directory_path: str) -> None:
    path = os.getcwd()
    os.chdir(directory_path)
    data = read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")

    x_data = [[i[0].split("-")] for i in data]
    with open('X.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(x_data)  

    y_data = [i[1:] for i in data]    
    with open('Y.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(y_data)
    os.chdir(path)


def distribution_by_year(directory_path: str) -> None:
    data = read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv") 
    print (data)     
    path = os.getcwd()
    os.chdir(directory_path)
    
    for year in data:
        year_data = data[data['date'] == year]
        output_file = f'{directory_path}/{year_data.iloc[0]["date"].strftime("%Y%m%d")}_{year_data.iloc[-1]["date"].strftime("%Y%m%d")}.csv'
    with open(output_file, 'w', encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(year_data)
    os.chdir(path)

def distribution_by_week(directory_path: str,file_path:str, start_day ) -> None:
    data = read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
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

if __name__ == "__main__":
    
    distribution_by_year(r"C:\Ycheba\2_kurs\LAB_Python\datasets")







'''подправить'''













'''

def growth(date1: str, date2: str) -> int:
    current_day = datetime.datetime.strptime(date1, '%Y-%m-%d').date()
    next_day = datetime.datetime.strptime(date2, '%Y-%m-%d').date()
    return (next_day - current_day).days


def distribution_date_and_data(directory_path: str) -> None:
    path = os.getcwd()
    os.chdir(directory_path)
    data = read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    x_data = [[i[0].split("-")] for i in data]
    y_data = [i[1:] for i in data]   
    with open('X.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(x_data)   
    with open('Y.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(y_data)
    os.chdir(path)


def distribution_by_year(directory_path: str) -> None:
    data = read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    year_list = []
    for day in data:
        year_list.append(int(day[0].split("-")[0]))
    year_list = sorted(list(set(year_list)))
    for year in year_list:
        data_year = [day for day in data if int(day[0].split("-")[0]) == year]
        a = "".join(data_year[0][0].split("-"))
        b = "".join(data_year[-1][0].split("-"))
        with open(f"{a}_{b}.csv", 'w', encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data_year)
    os.chdir(path)

def distribution_by_week(directory_path: str, start_day: int) -> None:
    data = read_data(r"C:\Ycheba\2_kurs\LAB_Python\datasets\dataset.csv")
    path = os.getcwd()
    os.chdir(directory_path)
    day_of_week = start_day
    data_week = [data[0]]
    for i in range(1, len(data) - 1):
        if day_of_week >= 7:
            a = "".join(data_week[0][0].split("-"))
            b = "".join(data_week[-1][0].split("-"))
            with open(f"{a}_{b}.csv", 'w', encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data_week)
            data_week.clear()
            data_week.append(data[i])
            day_of_week = growth(data[i-1][0], data[i][0])
            continue
        data_week.append(data[i])
        day_of_week += growth(data[i-1][0], data[i][0])
    a = "".join(data_week[0][0].split("-"))
    b = "".join(data_week[-1][0].split("-"))
    with open(f"{a}_{b}.csv", 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data_week)
    os.chdir(path)
    '''