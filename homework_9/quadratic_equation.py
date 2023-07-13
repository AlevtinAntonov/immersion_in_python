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
            lst_solution = []
            with open(file_name, 'r', encoding='utf-8') as csv_file:
                reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
                for row in reader:
                    x_1, x_2 = func(row[0], row[1], row[2])
                    lst_solution.append([row[0], row[1], row[2], x_1, x_2])
            return lst_solution

        return wrapper

    return deco


def save_results_to_json(func):
    file = Path(f"{func.__name__}.json")

    def wrapper(*args, **kwargs):
        lst_solution = [func(*args, **kwargs)]
        json_res = [dict(a=v[0], b=v[1], c=v[2], x_1=v[3], x_2=v[4]) for v in lst_solution[0]]
        with open(file, 'w', encoding='utf-8') as json_f:
            json.dump(json_res, json_f, indent=2)
        return lst_solution

    return wrapper


@save_results_to_json
@data_from_csv_wrap('random.csv')
def solving_quadratic_equation(a: int, b: int, c: int):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        x_1 = x_2 = 'None'
    elif a == 0:
        x_1, x_2 = -c / b, 'None'
    elif discriminant == 0:
        x_1, x_2 = -b / 2 * a, 'None'
    else:
        x_1, x_2 = (-b + discriminant ** .5) / (2 * a), (-b - discriminant ** .5) / (2 * a)
    return x_1, x_2


def generating_csv_file(file_name: str = 'random.csv'):
    number_of_rows = 100
    min_number = -100
    max_number = 100

    rows = []
    for _ in range(number_of_rows):
        a, b, c = random.sample(range(min_number, max_number), 3)
        rows.append([a, b, c])
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    solving_quadratic_equation()
    # generating_csv_file()
