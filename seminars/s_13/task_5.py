# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет
# есть ли он в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит получает его
# уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа,
# вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера

import json
from task3_v2 import User
from user_exeptions import LevelError, AccessError


class Project:
    def __init__(self, project_users=None):
        self.project_users = project_users or []
        self.admin = None

    @classmethod
    def fill_project_users(cls):
        with open('users.json', 'r', encoding='utf-8') as j:
            file = json.load(j)
            temp = []
            for key in file:
                for user in file[key].items():
                    temp.append(User(user[1], int(user[0]), int(key)))
            return cls(temp)

    def enter(self, name, id_, level):
        user = User(name, id_, level)
        if user not in self.project_users:
            raise AccessError(name, id_)
        if self.admin is None:
            self.admin = user
        for proj_user in self.project_users:
            if self.admin is not None:
                if user == proj_user and proj_user.level < self.admin.level:
                    self.admin = user

    def add_user(self, name, id_, level):
        if self.admin is None:
            print('Пользователь не добавлен! Для добавления пользователя войдите в систему.')
        elif level < self.admin.level:
            raise LevelError
        else:
            self.project_users.append(User(name, id_, level))

    def del_user(self, name, id_, level):
        if level < self.admin.level:
            raise LevelError
        try:
            self.project_users.remove(User(name, id_, level))
        except ValueError:
            print('Невозможно удалить запись! Пользователя нет в списке!')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file = open(f'project_users.json', 'w', encoding='utf-8')
        json.dump([repr(user) for user in self.project_users], self.file, ensure_ascii=False)
        self.file.close()


if __name__ == '__main__':
    with Project().fill_project_users() as p:
        print(p.project_users)
        p.add_user('Алевтин', 1001, 1)
        print(p.project_users)
        p.enter('Антон', 456, 2)
        p.enter('Андрей', 321, 4)
        p.enter('Иван', 123, 1)
        p.add_user('Алевтин', 1001, 1)
        print(p.project_users)
        print(f'Current admin - {p.admin=}')
        p.del_user('Алевтин', 1111, 1)
        p.enter('Аноним', 4567, 4)
