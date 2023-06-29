# Создайте функцию генератор всех чисел Фибоначчи (см. Википедию)

num = int(input('Введите номер элемента Фиббоначи: '))


def fibo_calc():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


my_iter = iter(fibo_calc())
for i in range(num):
    next(my_iter)
    if i == num - 1:
        print(next(my_iter))


