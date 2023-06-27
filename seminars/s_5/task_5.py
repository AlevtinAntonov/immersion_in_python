# Задание №5
# ✔ Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

print(*('FizzBuzz' if num % 15 == 0 else 'Buzz' if num % 5 == 0 else 'Fizz' if num % 3 == 0 else num for num in
        range(1, 101)))


def gen():
    for num in range(1, 101):
        if num % 15 == 0:
            yield 'FizzBuzz'
        elif num % 5 == 0:
            yield 'Buzz'
        elif num % 3 == 0:
            yield 'Fizz'
        else:
            yield num


print(*gen(), sep=' ')

gen_2 = ('Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or i for i in range(1, 101))
print(*gen_2)