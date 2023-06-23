# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте список по убыванию суммы цифр

lst = [123, 57, 1, 12]
res_lst = [57, 123, 12, 1]


def sum_sort(in_lst):
    return sorted(in_lst, key=sum_chr, reverse=True)


def sum_chr(number):
    return sum(map(int, str(number)))


def sum_sort_2(in_lst):
    return sorted(in_lst, key=lambda x: sum(map(int, str(x))), reverse=True)


print(sum_sort(lst))
print(sum_sort_2(lst))
