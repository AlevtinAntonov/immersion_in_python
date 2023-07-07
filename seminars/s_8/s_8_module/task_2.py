# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json

def read_user():
    while True:
        try:
            with open('users.json', 'r', encoding='utf-8') as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}
        u_id, level = None, None
        name = input('Input user name: ')
        is_valid_data = False
        while not is_valid_data:
            u_id, level = (i for i in input('Input spaced ID and LEVEL (1 to 7): ').split())
            if int(level) in range(1, 8):
                if users:
                    if all(u_id not in v.keys() for k, v in users.items()):
                        is_valid_data = True
                    else:
                        print('ID already exists! Try again!')
                else:
                    is_valid_data = True
            else:
                print('Invalid level! Try again!')
        if level not in users:
            users[level] = {}
        users[level][u_id] = name
        with open("users.json", "w") as f:
            json.dump(users, f)
            print('User added successfully!')


read_user()
