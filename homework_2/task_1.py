# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.
hex_number = 16
hex_base = '0123456789abcdef'
number = int(input('Введите целое число: '))
hex_result = ''

print(hex(number))

while number > 0:
    division_result = number % hex_number
    hex_result = hex_base[division_result] + hex_result
    number //= hex_number

print('0x' + hex_result)
