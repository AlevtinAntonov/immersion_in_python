# Задание №8
# ✔ Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

tourists = {
    'Alex': ('Палатка', 'Спальник', 'Фонарик', 'Миска', 'Хлеб', 'Карта'),
    'Oleg': ('Спальник','Спички', 'Миска', 'Кружка', 'Консервы', 'Компас'),
    'Dima': ('Спальник','Топор', 'Миска', 'Кружка', 'Крупа', 'Телефон', 'Батарейки')
}
one = list(tourists.values())
print(one)
def list_atribute_frends(dict_list):
    list_atribute = []
    for atribut in dict_list.values():
        list_atribute += atribut
    return list_atribute


# Какие вещи уникальны, есть только у одного друга
# и имя того, у кого данная вещь отсутствует
count = 0
# for i in list_atribute_frends(friends):
#     for j in list_atribute_frends(friends):
#         if j == i:
#             count += 1

def dict_unicum_atribute (dict_list):
    name_not_atribute = []
    new_dict = {}
    count = 0
    for key, value in tourists.items():
        name_not_atribute.append(key)
        new_dict[key] = []
        for j in value:
            for k in list_atribute_frends(tourists):
                if k == j:
                    count += 1
            if count == 1:
                new_dict[key] += [j]
            if count > 1:
                name_not_atribute.remove(key)
            count = 0
    print("у этого списка людей отсутствует вещь, которая дублируется у остальных", name_not_atribute)
    return new_dict

print(f"Вещи которые взяли три друга{sorted(set(list_atribute_frends(tourists)))}")
# print(f"Уникальные вещи которые взял каждый друг {dict_unicum_atribute(friends)}")
