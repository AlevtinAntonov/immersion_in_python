# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

num = int(input('Введите номер элемента Фиббоначи: '))


def fibo_calc():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print(f"Значение {num} элемента: ", *fibo_calc(num))
