# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.
# Для простоты будем использовать только положительную индексацию

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
ind_1 = 7
ind_2 = 3


def calc_amount(num_lst, ind_start, ind_end):
    ind_min = min(ind_start, ind_end)
    ind_max = max(ind_start, ind_end)
    if ind_min > 0 and ind_max < len(num_lst):
        res = sum(num_lst[ind_min:ind_max + 1:])
    elif ind_min < 0 and ind_max < len(num_lst):
        res = sum(num_lst[:ind_max + 1:])
    elif ind_min > 0 and ind_max >= len(num_lst):
        res = sum(num_lst[ind_min::])
    else:
        res = sum(num_lst)
    return res


print(calc_amount(numbers, ind_1, ind_2))


def test3(ls: list, i1: int, i2: int):
    i1, i2 = sorted((i1, i2))
    i1 = 0 if i1 > len(ls) else i1
    i2 = len(ls) if i2 > len(ls) else i2
    return sum(ls[i1:i2 + 1])


print(test3(numbers, ind_1, ind_2))
