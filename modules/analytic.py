import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('datasets/dataset.csv')

df.columns = ["Date", "Celsius temperature", "Pressure", "Direction", "Speed"]

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

df = df.dropna().reset_index(drop=True)

df['Fahrenheit temperature'] = 9/5 * df['Celsius temperature'] + 32


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


def average_monthly_temperature(df: pd.DataFrame, parametr: str) -> pd.Series | None:
    """
    Группировка по месяцам с вычислением среднего значения температуры
    Args:
      df: Dataframe с исходными значениями
      parametr: Столбец, указывающий, какая температура берется
    Returns:
      Ряд, показывающий среднее значение за все месяцы

    """
    if parametr in ["Celsius temperature", 'Fahrenheit temperature']:
        return df.groupby(df.Date.dt.month)[parametr].mean()


def show_temperature_graph(df: pd.DataFrame, parametr: str) -> None:
    """
    Отображение графика температуры за весь период
    Args:
      df: Dataframe с исходными значениями
      parametr: Столбец, указывающий, какая температура берется

    """
    if parametr in ["Celsius temperature", 'Fahrenheit temperature']:
        fig = plt.figure(figsize=(30, 5))
        plt.ylabel(parametr)
        plt.xlabel("date")
        plt.title('Изменение температуры')
        plt.plot(df["Date"], df[parametr], color='green', linestyle='-', linewidth=2)
        plt.show()


def show_monthly_temperature_statistics(df: pd.DataFrame, month: int, year: int) -> None:
    """
    Отображение графика температуры за указанный месяц в году
    и отображение медианы и средних значений
    Args:
      df: Dataframe с исходными значениями
      month: Месяц, для которого строится график температуры
      year: Год, для которого строится график температуры
      
    """
    month_df = df[(df.Date.dt.month == month) & (df.Date.dt.year == year)]
    fig = plt.figure(figsize=(30, 5))

    fig.add_subplot(1, 3, 1)
    plt.ylabel("Celsius temperature")
    plt.xlabel("Date")
    plt.plot(month_df.Date.dt.day, month_df["Celsius temperature"],
             color='green', linestyle='-', linewidth=2, label='Celsius temperature')
    plt.axhline(y=month_df["Celsius temperature"].mean(), color='yellow', label="Average value")
    plt.axhline(y=month_df["Celsius temperature"].median(), color='blue', label="Median")
    plt.legend(loc=2, prop={'size': 10})

    fig.add_subplot(1, 3, 2)
    plt.ylabel("Fahrenheit temperature")
    plt.xlabel("Date")
    plt.plot(month_df.Date.dt.day, month_df["Fahrenheit temperature"],
             color='red', linestyle='--', linewidth=2, label='Fahrenheit temperature')
    plt.axhline(y=month_df["Fahrenheit temperature"].mean(), color='yellow', label="Average value")
    plt.axhline(y=month_df["Fahrenheit temperature"].median(), color='blue', label="Median")
    plt.legend(loc=2, prop={'size': 10})

    plt.show()


if __name__ == "__main__":
    filtered_temp_df = filter_celsius_temp(df, 25)
    filtered_date_df = filter_by_date(df, '2023-01-01', '2023-12-31')
    show_monthly_temperature_statistics(df, 1, 2023)




