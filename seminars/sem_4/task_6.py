# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
index_1 = -1
index_2 = 12

def slice_amount(num_list, index_start, index_end):
    if index_start > 0 and index_end < len(num_list):
        res = sum(num_list[index_start:index_end+1:])
    elif index_start < 0 and index_end < len(num_list):
        res = sum(num_list[:index_end + 1:])
    elif index_start > 0 and index_end >= len(num_list):
        res = sum(num_list[index_start::])
    else:
        res = sum(num_list)

    return res
print(slice_amount(numbers, index_1, index_2))