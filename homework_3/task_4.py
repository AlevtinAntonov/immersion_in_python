# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

BACKPACK_CAPACITY = 10_000
things = {'спальник': 2000, 'пенка': 200, 'спички': 20, 'футболка': 300, 'термос': 1500, 'аптечка': 200,
          'бинокль': 400, 'удочка': 700, 'палатка': 3500, 'консервы': 2000, 'фонарик': 100, }

weight = 0
backpack_set = {}

for k, v in things.items():
    weight += int(v)
    if weight <= BACKPACK_CAPACITY:
        backpack_set[k] = v

print(f'В рюкзак вместимостью {BACKPACK_CAPACITY} г вместятся {len(backpack_set)} вещей:\n {backpack_set}')