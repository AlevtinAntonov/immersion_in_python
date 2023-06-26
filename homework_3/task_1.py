# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

TWO = 2
friends = {
    'Alex': ('Спальник', 'Миска', 'Спички', 'Фонарик', 'Карта', 'Палатка'),
    'Oleg': ('Спальник', 'Миска', 'Кружка', 'Спички', 'Консервы', 'Компас'),
    'Dima': ('Спальник', 'Миска', 'Кружка', 'Топор', 'Крупа', 'Телефон')
}
count = len(friends)
name_friends = []
for friend in friends:
    name_friends.append(friend)


def all_things(dict_name):
    common_set = set()
    for k, v in dict_name.items():
        common_set = common_set.union(set(v))
    return common_set


def unique_things(dict_name):
    unique_one_friend = dict()
    for name_friend in name_friends:
        other_things = set()
        for k, v in dict_name.items():
            if k != name_friend:
                other_things = other_things.union(set(v))

        unique_one_set = all_things(dict_name).difference(other_things)
        unique_one_friend.setdefault(name_friend, unique_one_set)

    return unique_one_friend


def all_friends_except_one(dict_name):
    except_one_friend = dict()
    unique_one_friend = unique_things(dict_name)

    for k, v in dict_name.items():
        intersection_set = set(v).difference(set(unique_one_friend[k]))
        except_one_friend.setdefault(k, intersection_set)

    all_repeat = []
    for k, v in except_one_friend.items():
        for i in v:
            all_repeat.append(i)

    new_list = []
    for i in all_repeat:
        if all_repeat.count(i) == TWO and not new_list.count(i):
            new_list.append(i)

    for i in range(len(new_list)):
        two_things_has_friends = set()
        two_things_has_friends.add(new_list[i])
        for k, v in except_one_friend.items():
            if len(two_things_has_friends.intersection(set(v))) == 0:
                print(f' У {k} нет -> {new_list[i]}, а двух остальных есть.')


print(f'Все три друга взяли: {all_things(friends)}')
print(f'Уникальные вещи есть только у одного друга- {unique_things(friends)}')
all_friends_except_one(friends)
