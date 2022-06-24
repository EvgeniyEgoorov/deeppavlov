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
   данными типа str - она отсеется (предполанается, что в колонках данные одного типа);
5) Внутри функции sum_checker() добавил метод fillna(0), который  заменит осутствующие данные объектов (если такие будут
   в .csv файле) на числовые значения (в нашем случае на 0)

"""


def sum_checker(data):
  return data.fillna(0).values.sum() == 10
  
def reader(path):
    try:
        df = pd.read_csv(path, header=None)
        return df.select_dtypes(include=['float64', 'int64'])
    except (pd.errors.EmptyDataError) as e:
        print("Файл пуст")
        raise e
    except (FileNotFoundError) as e:
        print("Файл не найден")
        raise e
    

if __name__ == '__main__':
    print(sum_checker(reader('data.csv')))
