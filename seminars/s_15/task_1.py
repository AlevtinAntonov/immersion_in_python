# Задание №1
# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='./logfiles/log.log', level=logging.ERROR, encoding='utf-8', filemode='a')
                    # format=f'{level_name:<5} : (time: {ask_time: }) - {message}')

logger = logging.getLogger(__name__)


def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        logging.error('Error!!')
        return float('inf') if x > 0 else float('-inf')
print(divide(-5, 0))