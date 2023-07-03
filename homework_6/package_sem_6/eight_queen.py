# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть
# ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
# число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной
# расстановки ферзей в задаче выше. Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок
from itertools import permutations

variant_1 = [(1, 1), (2, 5), (3, 8), (4, 6), (5, 3), (6, 7), (7, 2), (8, 4)]


def eight_queens():
    for p in permutations(range(1, 9)):
        yield [x for x in enumerate(p, start=1)]


def check_eight_queens(variant):
    if variant in eight_queens():
        return True
    return False


def all_eight_queens():
    for queen in eight_queens():
        err = False
        for i, j in ((i, j) for i in queen for j in queen if i[0] < j[0]):
            if abs(i[0] - j[0]) == abs(i[1] - j[1]):
                err = True
                break
        if not err:
            print(queen)

all_eight_queens()
print(check_eight_queens(variant_1))