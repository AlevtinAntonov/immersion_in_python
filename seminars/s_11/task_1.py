# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
import time


class MyStr(str):
    """Класс Моя Строка, где: доступны все возможности str дополнительно хранятся имя автора строки и
    время создания (time.time)"""
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.start_time = time.time()
        return instance

    def __str__(self):
        return f'{self.value} Name {self.name}, time {self.start_time}'


str_1 = MyStr('5', 'Alex')
print(str_1)
# str_2 = MyStr('Second')
# print(str_2)
