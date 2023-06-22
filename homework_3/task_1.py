# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.


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
    unique_set = set()
    count = len(dict_name)
    other_things = set()
    friend_name = 'Alex'
    for name_friend in name_friends:
        for k, v in dict_name.items():
            if k != name_friend:
                other_things = other_things.union(set(v))
            unique_one_set = all_things(dict_name).difference(other_things)
            unique_set = unique_set.union(unique_one_set)

    return unique_set


    #
    # for k, v in dict_name.items():
    #     unique_set = set(dict_name[k]).difference()

    # pass

def all_friends_except_one(dict_name):
    pass

unique_set = set(friends['Alex']).difference(set(friends['Oleg']) | (set(friends['Dima'])))


    # difference_set = common_set.difference(set(v))
    # intersection_set = intersection_set.intersection(set(v))

print(f'Все три друга взяли: {all_things(friends)}')
print(f'Уникальные вещи есть только у одного друга- {unique_things(friends)}')
print(f'Вещи уникальны: {unique_set}')
# print(f'ПЕресечение: {sorted(intersection_set)}')


# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = } union')
# print()
#
my_set = {3, 4, 2, 5, 6, 1, 7}
other_set = {1, 4, 42, 314}
new_set = my_set.intersection(other_set)
print(f'{my_set = }\n{other_set = }\n{new_set = } intersection ')
print()
#
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.difference(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = } difference ')
##########################

# tourists = {
#     'Alex': ('Палатка', 'Спальник', 'Фонарик', 'Миска', 'Хлеб', 'Карта'),
#     'Oleg': ('Спальник','Спички', 'Миска', 'Кружка', 'Консервы', 'Компас'),
#     'Dima': ('Спальник','Топор', 'Миска', 'Кружка', 'Крупа', 'Телефон', 'Батарейки')
# }
# one = list(tourists.values())
# print(one)
# def list_atribute_frends(dict_list):
#     list_atribute = []
#     for atribut in dict_list.values():
#         list_atribute += atribut
#     return list_atribute
#
#
# # Какие вещи уникальны, есть только у одного друга
# # и имя того, у кого данная вещь отсутствует
# count = 0
# # for i in list_atribute_frends(friends):
# #     for j in list_atribute_frends(friends):
# #         if j == i:
# #             count += 1
#
# def dict_unicum_atribute (dict_list):
#     name_not_atribute = []
#     new_dict = {}
#     count = 0
#     for key, value in tourists.items():
#         name_not_atribute.append(key)
#         new_dict[key] = []
#         for j in value:
#             for k in list_atribute_frends(tourists):
#                 if k == j:
#                     count += 1
#             if count == 1:
#                 new_dict[key] += [j]
#             if count > 1:
#                 name_not_atribute.remove(key)
#             count = 0
#     print("у этого списка людей отсутствует вещь, которая дублируется у остальных", name_not_atribute)
#     return new_dict
#
# print(f"Вещи которые взяли три друга{sorted(set(list_atribute_frends(tourists)))}")
# # print(f"Уникальные вещи которые взял каждый друг {dict_unicum_atribute(friends)}")
