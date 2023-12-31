# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.
hex_number = 16
hex_base = '0123456789abcdef'
number = int(input('Введите целое число: '))
hex_result = ''

print(hex(number))

while number:
    # hex_result = hex_base[number % hex_number] + hex_result
    # number //= hex_number
    number, remainder = divmod(number, hex_number)
    hex_result = hex_base[remainder] + hex_result

print('0x' + hex_result)
