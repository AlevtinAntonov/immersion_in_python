# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь
from task_3 import Person


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id_num: int):
        super().__init__(last_name, first_name, patronymic, age)
        self.id_num = id_num
        self.level = self._level()

    def _level(self):
        return sum(int(i) for i in str(self.id_num)) % 7


if __name__ == '__main__':
    man = Employee("Иванов", "Иван", "Иванович", 40, 555555)
    print(man.full_name())
    print(man.id_num, man._level())
