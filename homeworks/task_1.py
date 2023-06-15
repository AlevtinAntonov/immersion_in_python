# Задание №9
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

print("{:^50}".format("ТАБЛИЦА УМНОЖЕНИЯ"))

for row in range(2, 11):
    print(*(f"{col} X {row:2d} = {row * col:2d} " for col in range(2, 6)))
print()
for row in range(2, 11):
    print(*(f"{col} X {row:2d} = {row * col:2d} " for col in range(6, 10)))
