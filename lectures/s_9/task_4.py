# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.

from typing import Callable


def counter_wrap(count: int):
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return deco


@counter_wrap(2)
def test_func():
    print("test_func")


if __name__ == '__main__':
    test_func()