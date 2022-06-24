import pandas as pd

"""
1) Для более удобного тестирования разбил логику на отдельные функции:
   reader() - читает csv файл,
   sum_checker() проверяет сумму;
2) Путь к файлу передаем в reader() в качетсве аргумента, так скрипт может быть использован для чтения любого другого 
   .csv файла;
3) Обернул метод read_csv() в конструкцию try/except - функция будет поднимать ошибку если указанный файл не найден, 
   или пуст;
4) С помощью select_dtypes в функцию sum_checker передаем данные типа int и float, если в .csv файле будет колонка с 
   данными типа str - она отсеется;
5) Внутри функции sum_checker() добавил метод fillna(0), который  заменит осутствующие данные объектов (если такие будут
   в .csv файле) на числовые значения (в нашем случае на 0)

"""


def sum_checker(data):
    return data.fillna(0).values.sum() == 10


def reader(path):
    try:
        df = pd.read_csv(path, header=None)
        print(sum_checker(df.select_dtypes(include=['float64', 'int64'])))
    except (pd.errors.EmptyDataError,
            FileNotFoundError) as e:
        print("Testing multiple exceptions. {}".format(e.args[-1]))


reader('data.csv')
