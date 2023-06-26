# Задание №8
# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.


def replacement_with_s(*words):
    words = list(words)
    temp = []
    for i in range(len(words)):
        if words[i].endswith('s') and words[i] != 's':
            temp.append(words[i])
            words[i] = None
    for i in range(len(words)):
        if words[i] is not None:
            words[i] += ''.join([i for i in temp])
    return words


print(replacement_with_s('ноs', 'рот', 'насоs', 's'))

# Напишите функцию для транспонирования матрицы

def transparent_matrix(*a_list: list[[int]]) -> list[()] | str:
    is_transparent = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            is_transparent = False
    if is_transparent:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспорировать'


print(transparent_matrix([1, 3, 5], [2, 4, 6]))

# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def hashable_dicts(**kwargs):
    pets = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        pets[v] = k
    return pets


print(hashable_dicts(dog='Jack', cat={'Leopold': 2, 'Murka': 3}, turtle=['bill', 'jack', 'anatoliy'],
                     hamster={'edward', 'homa'}))
