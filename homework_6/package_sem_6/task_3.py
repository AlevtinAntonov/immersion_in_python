# Задание №3
# � Улучшаем задачу 2
# � Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# � Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# � Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
import sys
from task_2 import game

arg = list(map(int, sys.argv[1:]))
print(game(*arg))


