# Задание №2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
from pathlib import Path


def check_user():
    """
    ask data from user and add to json file
    :return:
    """
    if Path('out/task_2.json').exists():
        with open('out/task_2.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
    else:
        file = {str(k): {} for k in range(1, 8)}
    while True:
        inp = input(" please enter name id level :")
        if not inp:
            break
        name, id_, access = inp.split()
        file[access].update({id_: name})
    with open('out/task_2.json', 'w', encoding='utf-8') as f:
        json.dump(file, f)

check_user()