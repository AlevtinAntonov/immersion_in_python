# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

num = int(input('Введите номер элемента Фиббоначи: '))


def fibo_calc(n):
    n = int(n) - 2
    a = b = 1
    while n:
        a, b = b, a + b
        n -= 1
    yield b


print(f"Значение {num} элемента: ", *fibo_calc(num))
