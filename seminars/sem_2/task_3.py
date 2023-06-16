# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

number = int(input('Введите целое число: '))
bin_base = 2
oct_base = 8
bin_result = ''
oct_result = ''
number_1, number_2 = number, number
print(number, bin(number), oct(number))

while number_1 > 0:
    bin_result = str(number_1 % bin_base) + bin_result
    number_1 //= bin_base

while number_2 > 0:
    oct_result = str(number_2 % oct_base) + oct_result
    number_2 //= oct_base

print(number, bin_result, oct_result)
