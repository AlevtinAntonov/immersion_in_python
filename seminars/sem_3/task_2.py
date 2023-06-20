# Задание №3
# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях
user_input = input('Введите что-нибудь из условия: ')

if user_input.isdigit():
    result = 'Целое'
    val = int(user_input)
elif user_input.isdigit() and user_input.count('.') == 1:
    result = 'Вещественное'
    val = float(user_input)
elif any(map(str.isupper, user_input)):
    result = 'Заглавная буква есть'
    val = user_input.lower()
else:
    result = user_input.lower()
    val = user_input.lower()
    print('Else')
print(f'{result=},  {val=}')