# Задание №2
# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint



result = None
player_number = None
count = 1

def game(start, end, steps):
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    while count <= NUMBER_OF_ATTEMPTS:
        player_number = int(input(f'{count} попытка. Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
        if LOWER_LIMIT <= player_number <= UPPER_LIMIT:
            if player_number == number:
                result = 'Вы угадали число!!!'
                break
            elif player_number > number:
                result = 'Ваше число больше загаданного'
            else:
                result = 'Ваше число меньше загаданного'
        print(result)
        count += 1


if __name__ == '__main__':
    game()


