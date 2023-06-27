# Полезные однострочники
# a, b = b, a

# a, b, c = input("Три символа: ")
# print(f'{a=} {b=} {c=}')


a, b, c = ("один", "два", "три",)
print(f'{a=} {b=} {c=}')

# a, b, c = {"один", "два", "три", "четыре", "пять"}
# print(f'{a=} {b=} {c=}') # ValueError: too many values to unpack (expected 3)

# Распаковка коллекции с упаковкой “лишнего”, упаковка со звёздочкой
data = ["один", "два", "три", "четыре", "пять", "шесть", "семь",
]
a, b, c, *d = data
print(f'{a=} {b=} {c=} {d=}')
a, b, *c, d = data
print(f'{a=} {b=} {c=} {d=}')
a, *b, c, d = data
print(f'{a=} {b=} {c=} {d=}')
*a, b, c, d = data
print(f'{a=} {b=} {c=} {d=}')

link = 'https://docs.python.org/3/faq/programming.html#how-can-i-pass-optional-or-keyword-parameters-from-one-function-to-another'
prefix, *_, suffix = link.split('/')

# Распаковка со звёздочкой
data = [2, 4, 6, 8, 10, ]
for item in data:
print(item, end='\t')

data = [2, 4, 6, 8, 10, ]
print(*data, sep='\t')

# Множественное присваивание
a = b = c = 0
a += 42
print(f'{a=} {b=} {c=}')

a = b = c = {1, 2, 3}
a.add(42)
print(f'{a=} {b=} {c=}')

a, b, c = 1, 2, 3
print(f'{a=} {b=} {c=}')

t = 1, 2, 3
print(f'{t=}, {type(t)}')

# Множественное сравнение
a = b = c = 42
# if a == b and b == c:
if a == b == c:
print('Полное совпадение')

if a < b < c:
print('b больше a и меньше c')

# Плохие однострочник
# a = 12; b = 42; c = 73
# if a < b < c: b = None; print('Ужасный код')
# Задание
# data = {10, 9, 8, 1, 6, 3}
# a, b, c, *d, e = data
# print(a, b, c, d, e)

# Итераторы
# Функции iter() и next()
# Функция iter

a = 42
iter(a) # TypeError: 'int' object is not iterable

data = [2, 4, 6, 8]
list_iter = iter(data)
print(list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data)
print(*list_iter)
print(*list_iter)

data = [2, 4, 6, 8]
list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable

import functools
f = open('mydata.bin', 'rb')
for block in iter(functools.partial(f.read, 16), b''):
print(block)
f.close()

# Функция next
data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter))
print(next(list_iter)) # StopIteration

data = [2, 4, 6, 8]
list_iter = iter(data)
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))
print(next(list_iter, 42))

# Задание
# data = {"один": 1, "два": 2, "три": 3}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)

# Генераторы
a = range(0, 10, 2)
print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
b = range(-1_000_000, 1_000_000, 2)
print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')

# Генераторные выражения
my_gen = (chr(i) for i in range(97, 123))
print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
for char in my_gen:
    print(char)

# Комбинации for и if в генераторах и выражениях
# gen = (expression for expr in sequense1 if condition1
# for expr in sequense2 if condition2
# for expr in sequense3 if condition3
# # ...
# for expr in sequenseN if conditionN)

# for expr in sequense1:
#     if not condition1:
#         continue
#     for expr in sequense2:
#         if not condition2:
#             continue
# # ...
#         for expr in sequenseN:
#             if not conditionN:
#                 continue

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
res = list(mult)
print(f'{len(res)=}\n{res}')

# List comprehensions

my_listcomp = [chr(i) for i in range(97, 123)]
print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
for char in my_listcomp:
print(char)

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = []
# for item in data:
#     if item % 2 == 0:
#         res.append(item)
# print(f'{res = }')

data = [2, 5, 1, 42, 65, 76, 24, 77]
res = [item for item in data if item % 2 == 0]
print(f'{res = }')

# Генераторные выражения или генерация списка
x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = [i + j for i in x if i % 2 != 0 for j in y if j != 1]
print(f'{len(res)=}\n{res}')

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
for item in mult:
    print(f'{item = }')

# Set comprehensions
my_setcomp = {chr(i) for i in range(97, 123)}
print(my_setcomp) # {'f', 'g', 'b', 'j', 'e',... }
for char in my_setcomp:
    print(char)

x = [1, 1, 2, 3, 5, 8, 13]
y = [1, 2, 6, 24, 120, 720]
print(f'{len(x)=}\t{len(y)=}')
res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
print(f'{len(res)=}\n{res}')

# Dict comprehensions
my_dictcomp = {i: chr(i) for i in range(97, 123)}
print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
for number, char in my_dictcomp.items():
    print(f'dict[{number}] = {char}')

# Создание функции генератора
def factorial(n):
    number = 1
    result = []
    for i in range(1, n + 1):
        number *= i
        result.append(number)
    return result

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Команда yield
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i
        yield number

for i, num in enumerate(factorial(10), start=1):
    print(f'{i}! = {num}')

# Функции iter и next для генераторов
my_iter = iter(factorial(4))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) # StopIteration

