# Задание №3
# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

import json
from typing import Callable
from pathlib import Path


def to_json_wrapper(func) -> Callable[[], None]:
    file = Path(f"{func.__name__}.json")
    if file.is_file():
        with open(file, 'r', encoding='utf-8') as f:
            json_file = json.load(f)
    else:
        json_file = []

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        dct = {'args': args, **kwargs, 'result': result}
        json_file.append(dct)
        with open(file, 'a', encoding='utf-8') as json_f:
            json.dump(json_file, json_f, indent=2)
        return result

    return wrapper


@to_json_wrapper
def test_func(a: int, b: str, c: int):
    return str(a) + b + str(c)


if __name__ == '__main__':
    test_func(1, '2', 3)
    test_func(3, '4', 5)

# result = {'args': args,
#         'kwargs': kwargs,
#         'result': func_res}