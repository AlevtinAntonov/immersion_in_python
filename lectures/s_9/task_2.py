# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from typing import Callable
from random import randint


def deco_guess_number(func):
    def wrapper(num: int, count: int):
        if not 1 <= num <= 100:
            print(num)
            num = randint(1, 100)
        if not 1 <= count <= 10:
            count = randint(1, 10)
        result = func(num, count)
        return result

    return wrapper

@deco_guess_number
def game(num: int, count: int):
    for i in range(1, count + 1):
        print(f"Попытка номер {i} ")
        user_num = int(input("Введите число от 1 до 100: "))
        if user_num == num:
            return "Вы угадали!"
        elif user_num < num:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")


if __name__ == '__main__':
    game(101, 5)
