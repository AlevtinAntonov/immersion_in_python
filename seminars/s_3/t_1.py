# Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные
# (без повтора) элементы исходного списка.

# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

my_list = [2, 2, 5, 6, 8, 4, 6, 7, 8, 6, 2, 1]
list_2 = []

for i in my_list:
    if i not in list_2:
        list_2.append(i)
print(my_list)
print(list_2)

list_3 = list(set(my_list))
print(list_3)

list_4 = list(dict.fromkeys((my_list)))
print(list_4)