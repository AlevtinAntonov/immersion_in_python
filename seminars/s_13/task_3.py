# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.
# Вспомните задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей

class User:
    def __init__(self, name, user_id, level=None):
        self.name = name
        self.user_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __repr__(self):
        print(f'User {self.name} {self.user_id} {self.level}')


if __name__ == '__main__':
    e1 = User('asd', 1, 3)
    e2 = User('zxc', 3, 5)
    e1.__repr__()
    e2.__repr__()
    print(e1.level > e2.level)
