# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4]
sort_list = sorted(my_list)
count = 2
for item in sort_list:
    if sort_list.count(item) == count:
        my_list.remove(item)

print(my_list)
