# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

my_list = [1, 1, 2, 2, 2, 3, 4, 8, 7, 7, 4]
new_list = []

for index, value in enumerate(my_list, start=1):
    if value % 2 != 0:
        new_list.append(index)

print(new_list)