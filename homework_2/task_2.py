# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

print(Fraction(5, 16) + Fraction(7, 12))
# def calculate_lcd(x, y):
#     if x > y:
#         greater = x
#     else:
#         greater = y
#     while True:
#         if greater % x == 0 and greater % y == 0:
#             lowest_common_d = greater
#             break
#         greater += 1
#     return lowest_common_d
#
# def add_multiplier(x, y, lcd):
#     add_multiplier_1 = lcd / x
#     add_multiplier_2 = lcd / y
#     return add_multiplier_1, add_multiplier_2
#
# def greater_common_divider(x, y):
#     while y:
#         x, y = y, x % y
#     return x
#
input_fractions = input('Введите две дроби через пробел в формате - a/b c/d ').split()

fraction_1, fraction_2 = map(str, input_fractions)
a, b = map(int, str(fraction_1).split('/'))
c, d = map(int, str(fraction_2).split('/'))
# lowest_common_denominator = calculate_lcd(b, d)
#
#
# add_multiplier_1, add_multiplier_2 = add_multiplier(b, d, lowest_common_denominator)
# e = int(a * add_multiplier_1 + c * add_multiplier_2)
#
#
# print(f'Cумма дробей {a}/{b} и {c}/{d} = {e}/{lowest_common_denominator}')

def lcm(a, b):
    """Нахождение наименьшего общего кратного двух чисел"""
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // gcd(a, b)
def gcd(a, b):
    """Нахождение наибольшего общего делителя двух чисел"""
    while b:
        a, b = b, a % b
    return a


def add_fractions(a, b, c, d):
    """Сложение двух дробей"""
    # Находим общий знаменатель
    common_denominator = lcm(b, d)

    # Приводим первую дробь к общему знаменателю
    a *= common_denominator // b
    b = common_denominator

    # Приводим вторую дробь к общему знаменателю
    c *= common_denominator // d
    d = common_denominator

    # Складываем дроби
    numerator = a + c

    # Сокращаем дробь
    divisor = gcd(numerator, common_denominator)
    numerator //= divisor
    common_denominator //= divisor

    return numerator, common_denominator

l, m = add_fractions(a,b,c,d)
print(l, m)


