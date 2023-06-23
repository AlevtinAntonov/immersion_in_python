# Задание №3
# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

text = '48 57'


def my_func(in_text):
    my_dict = dict()
    start, stop = map(int, in_text.split())

    for i in range(min(start, stop), max(start, stop) + 1):
        my_dict[chr(i)] = i
    return my_dict


print(my_func(text))
