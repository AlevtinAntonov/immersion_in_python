# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
MIN_NUMBER = 2
MIDDLE_NUMBER = 5
MAX_NUMBER = 9

print("{:^50}".format("ТАБЛИЦА УМНОЖЕНИЯ"))

for row in range(MIN_NUMBER, MAX_NUMBER + 1):
    print(*(f"{col} X {row:2d} = {row * col:2d} " for col in range(MIN_NUMBER, MIDDLE_NUMBER + 1)))
print()
for row in range(MIN_NUMBER, MAX_NUMBER + 1):
    print(*(f"{col} X {row:2d} = {row * col:2d} " for col in range(MIDDLE_NUMBER + 1, MAX_NUMBER + 1)))
