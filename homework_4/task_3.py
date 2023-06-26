# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ
# не хешируем, используйте его строковое представление.



def func(**kwargs):
    return {v if v.__hash__ is not None else str(v): k for k, v in kwargs.items()}


print(func(datas=[42, -73, 12, 85, -15, 2], s='Hello World', names=('NoName', 'OtherName', 'NewName'), sx=42))
