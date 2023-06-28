# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


num = int(input('Введите целое число: '))

fibo_nums = []
a, b = 0, 1

for i in range(num):
    fibo_nums.append(a)
    a, b = b, a + b

print(*fibo_nums)
