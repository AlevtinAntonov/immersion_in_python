# Задание №3
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента, значение — список элементов данного типа.
my_tuple = (True, False, 'one', 'two', 3, 2, 5.5, 6.5, [1, 2, 3], (5, 6, 9), (7, 6, 9),
            {1: 1, 2: 2, 3: 3}, {1: 10, 2: 8})
my_dict = {}

for item in my_tuple:
    if type(item) not in my_dict:
        my_dict[type(item)] = []
    my_dict[type(item)].append(item)
for key, val in my_dict.items():
    print(key, val)


