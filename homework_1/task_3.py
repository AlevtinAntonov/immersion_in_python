# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только
# на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
MIN_NUMBER = 1
MAX_NUMBER = 100_000
QUANTITY_OF_DIVISORS_OF_PRIME_NUMBER = 2
result = None

while True:
    number = int(input('Введите целое число от 1 до 100 000 : '))
    if MIN_NUMBER <= number <= MAX_NUMBER:
        break

for i in range(2, int((number ** 0.5) + 1)):
    if number % i == 0:
        result = 'составное'
        break
    else:
        result = 'простое'

print(f'Число {number} -> {result}')
