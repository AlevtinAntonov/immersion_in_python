# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только
# на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
MIN_NUMBER = 1
MAX_NUMBER = 100_000
QUANTITY_OF_DIVISORS_OF_PRIME_NUMBER = 2
while True:
    number = int(input('Введите целое число от 1 до 100 000 : '))
    if MIN_NUMBER <= number <= MAX_NUMBER:
        break

dividers = []
for i in range(1, int((number ** 0.5) + 1)):
    if i * i == number:
        dividers.append(i)
    elif number % i == 0:
        dividers.append(i)
        dividers.append(number // i)

if len(dividers) == QUANTITY_OF_DIVISORS_OF_PRIME_NUMBER:
    result = 'простое'
else:
    result = 'составное'

print(f'Число {number} -> {result} и имеет {len(dividers)} делителя(ей)')
