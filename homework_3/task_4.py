# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

BACKPACK_CAPACITY = 3_000
MIN_CAPACITY = 2_000
things = {'спальник': 2000, 'пенка': 200, 'спички': 20, 'футболка': 300, 'термос': 1500, 'аптечка': 200,
          'бинокль': 400, 'удочка': 700, 'палатка': 5500, 'консервы': 2000, 'фонарик': 100, }

sorted_things = dict(sorted(things.items(), key=lambda val: val[1]))
weight = 0
backpack_set = {}
list_weight = []
for k, v in things.items():
    list_weight.append(int(v))
    if weight <= BACKPACK_CAPACITY:
        print(weight, int(v))
        weight += int(v)
        backpack_set[k] = v

print(len(backpack_set),backpack_set, weight)

from itertools import combinations
def combine(dict, d):
    return list(combinations(dict,d))

dictA = { 1: 19, 2: 21, 3: 18, 4: 25, 5: 30,}
set = 4
print(combine(dictA, set))

def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s <= target and s > MIN_CAPACITY:
        print(f"Weight > {MIN_CAPACITY} and < {target} set = {partial} " )
    if s > target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        subset_sum(remaining, target, partial + [n])


subset_sum(list_weight, BACKPACK_CAPACITY)