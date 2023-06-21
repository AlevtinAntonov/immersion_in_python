# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

fraction_1, fraction_2, signs = input('Введите две дроби через пробел и знак + или * в формате - a/b c/d + ').split()
a, b = map(int, fraction_1.split('/'))
c, d = map(int, fraction_2.split('/'))

if not b or not d:
    print('На ноль делить нельзя!')
else:
    print('Fractions сумма: ', Fraction(a, b) + Fraction(c, d))
    print('Fractions произведение: ', Fraction(a, b) * Fraction(c, d))


def lowest_common_multiple(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // greatest_common_divisor(a, b)


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def fraction_reduction(numerator, common_denominator):
    divisor = greatest_common_divisor(numerator, common_denominator)
    numerator //= divisor
    common_denominator //= divisor

    return numerator, common_denominator

def check_result(numerator, denominator):
    if numerator >= denominator:
        numerator %= greatest_common_divisor(numerator, denominator)



def calc_fractions(a, b, c, d):
    match signs:
        case '+':
            common_denominator = lowest_common_multiple(b, d)
            a *= common_denominator // b
            c *= common_denominator // d
            numerator = a + c
            numerator, common_denominator = fraction_reduction(numerator, common_denominator)
        case '*':
            numerator = a * c
            common_denominator = b * d
            numerator, common_denominator = fraction_reduction(numerator, common_denominator)
    return numerator, common_denominator


numerator, denominator = calc_fractions(a, b, c, d)

if denominator == 0:
    print_res = 'На ноль делить нельзя!'
elif numerator == 0:
    print_res = 0
elif denominator == 1:
    print_res = numerator
else:
    print_res = f'{numerator}/{denominator}'

print(f'Результат {a}/{b} {signs} {c}/{d} = {print_res}')
