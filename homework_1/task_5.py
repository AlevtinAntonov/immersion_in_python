# 5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1001
NUMBER_OF_ATTEMPTS = 10

number = randint(LOWER_LIMIT, UPPER_LIMIT)
result = None
player_number = None
count = 1

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

print(f'Ваше число - {player_number} - {result}, загаданное число -> {number}')
