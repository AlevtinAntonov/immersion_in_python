# Задание №2
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint


def game(start_, end_, steps_):
    number = randint(start_, end_ + 1)
    while steps_:
        player_number = int(input(f'{steps_} попытка. Введите число: '))
        if start_ <= player_number <= end_:
            if player_number == number:
                return True
            elif player_number > number:
                result = 'Ваше число больше загаданного'
            else:
                result = 'Ваше число меньше загаданного'
        print(result)
        steps_ -= 1
    else:
        return False


if __name__ == '__main__':
    start, end, steps = 1, 100, 10
    game(start, end, steps)
