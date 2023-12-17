import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def process_data(path: str) -> pd.DataFrame:
    """
    Считывание и обработка в соответствии с вариантом данных из набора данных
    Args:
      path: путь к файлу для считывания информации
    Returns:
      Dataframe без значений Nan и с добавлением столбца температуры по Фаренгейту
    """
    df = pd.read_csv(path)
    df.columns = ["Date", "Celsius temperature", "Pressure", "Direction", "Speed"]
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
    df = df.dropna().reset_index(drop=True)
    df['Fahrenheit temperature'] = 9/5 * df['Celsius temperature'] + 32
    return df


def describe_column(df: pd.DataFrame, parametr: str) -> pd.Series | None:
    """
    Получение статистической информации
    Args:
      df: Dataframe с исходными значениями
      parametr: имя столбца фрейма данных, для которого находится статистическое описание
    Returns:
      Ряд, содержащий статистическое описание
    """
    if parametr in df.columns:
        return df[parametr].describe()
    else:
        return None


def filter_celsius_temp(df: pd.DataFrame, celsius_temp: int) -> pd.DataFrame:
    """
    Фильтрация по столбцу температура в градусах Цельсия
    Args:
      df: Dataframe с исходными значениями
      celsius_temp: температура в градусах Цельсия
    Returns:
      Dataframe с днями, в течение которых температура не ниже заданной
    """
    return df[df["Celsius temperature"] >= celsius_temp]


def filter_by_date(df: pd.DataFrame, end_date: str, start_date: str) -> pd.DataFrame:
    """
    Фильтрация по дате
    Args:
      df: Dataframe с исходными значениями
      start_date: Дата начала
      end_date: Дата окончания
    Returns:
      Dataframe с днями в диапазоне [start_date; end_date]
    """
    start_date = pd.to_datetime(start_date, format='%Y-%m-%d')
    end_date = pd.to_datetime(end_date, format='%Y-%m-%d')
    return df[(start_date <= df["Date"]) & (df["Date"] <= end_date)]





