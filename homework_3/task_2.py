# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов

new_list = [1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 7, 8, 9, 10, 11, 'one', 'one']

duplicate = {x for x in new_list if new_list.count(x) > 1}
print(duplicate)
