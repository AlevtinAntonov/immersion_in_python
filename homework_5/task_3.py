# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


num = int(input('Введите целое число: '))


def fibo_calc(num):
    fibo_nums = []
    a, b = 0, 1

    for i in range(num):
        fibo_nums.append(a)
        a, b = b, a + b
    yield fibo_nums


print(*fibo_calc(num))
