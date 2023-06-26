# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

text = '48 57'


def my_func(in_text):
    key_list = []
    value_list = []
    for item in sorted(in_text.split()):
        value_list.append(item)
    for item in (ord(chr) for chr in sorted(in_text)):
        key_list.append(item)
    uni_dict = dict(zip(key_list, value_list))

    return uni_dict


print(my_func(text))

