# Задание №3
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
user_input = input('Введите что-нибудь из условия: ')
# user_input = "-5.5665654654654"

if user_input.isdecimal():
    result = 'Целое'
    val = int(user_input)
elif user_input.replace('.', '').replace('-', '').isdecimal() and user_input.count('.') == 1 and \
        user_input.count('-') <= 1 and user_input[-1] != '.' and user_input[1:].count('-') == 0:
    if user_input[0] == '-':
        result = 'Вещественное отрицательное'
    else:
        result = 'Вещественное положительное'
    val = float(user_input)

elif any(map(str.isupper, user_input)):
    result = 'Заглавная есть'
    val = user_input.lower()
else:
    result = 'Остальной случай'
    val = user_input.upper()

print(f'{result=},  {val=}')
