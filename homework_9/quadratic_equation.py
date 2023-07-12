# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import random
from functools import wraps
from pathlib import Path
from typing import Callable

def data_from_csv_wrap(file_name: str):
    def deco(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file_name, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file)
                for i, row in enumerate(reader):
                    if i == 0:
                        continue
                    args = (int(j) for j in row)
                    result = func(*args, **kwargs)
                    yield result

        return wrapper

    return deco


def save_results_to_json(func):
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def wrapper(*args, **kwargs):
        for result in func(*args, **kwargs):
            if result:
                dct = {'args': args,
                       'kwargs': kwargs,
                       'result': str(result)}
                json_file.append(dct)
                with open(file, 'w', encoding='utf-8') as json_f:
                    json.dump(json_file, json_f, indent=2)
            else:
                break

    return wrapper
@save_results_to_json
@data_from_csv_wrap('random.csv')
def solving_quadratic_equation(a: int, b: int, c: int):
    """
        Решает квадратное уравнение ax^2 + bx + c = 0

        :param a: коэффициент при x^2
        :param b: коэффициент при x
        :param c: свободный член
        :return: корни уравнения
        """
    discriminant = b ** 2 - 4 * a * c
    print(discriminant)
    if a == 0:
        x = -c / b
        return x
    elif discriminant < 0:
        return 'Нет решения'
    elif discriminant == 0:
        x = -b / 2 * a
        return x
    else:
        x_1 = (-b + discriminant ** .5) / (2 * a)
        x_2 = (-b - discriminant ** .5) / (2 * a)
        return x_1, x_2


def generating_csv_file(file_name: str = 'random.csv'):
    number_of_rows = 100
    min_number = -100
    max_number = 100

    rows = []
    for _ in range(number_of_rows):
        a, b, c = random.sample(range(min_number, max_number), 3)
        rows.append({'a': a, 'b': b, 'c': c})
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['a', 'b', 'c'])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    solving_quadratic_equation()
    # generating_csv_file()
