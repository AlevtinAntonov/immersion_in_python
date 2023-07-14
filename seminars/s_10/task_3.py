# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения # возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст

class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def get_age(self):
        return self.__age

if __name__ == '__main__':
    man = Person("Иванов", "Иван", "Иванович", 40)
    print(man.get_age())
    print(man.full_name())
    man.birthday()
    print(man.get_age())
