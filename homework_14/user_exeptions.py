class UserException(Exception):
    pass


class LevelError(UserException):
    def __init__(self, level):
        self.level = level or None

    def __str__(self):
        return f"Ошибка уровня доступа - уровень доступа - {self.level}"


class AccessError(Exception):
    def __init__(self, name, id_):
        self.name = name
        self.id_ = id_

    def __str__(self):
        return f'Пользователь - {self.name} с ID - {self.id_} не существует. В доступе отказано!'
