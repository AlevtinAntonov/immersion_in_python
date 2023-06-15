# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только
# на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

while True:
    number = int(input('Введите целое число от 1 до 100 000 : '))
    if 1 <= number <= 100_000:
        break

dividers = []
for i in range(1, int((number ** 0.5) + 1)):
    if i * i == number:
        dividers.append(i)
    elif number % i == 0:
        dividers.append(i)
        dividers.append(number // i)

if len(dividers) == 2:
    print(f'Число {number} -> простое')
else:
    print(f'Число {number} -> составное и имеет {len(dividers)} делителей')
