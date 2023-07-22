# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
from typing import TypeAlias
from student import Student
import json

data_dict: TypeAlias = dict[str, dict[str, dict[str, str]]]
subjects_file = 'subject.csv'
json_data_file = 'students.json'


def loader(file_name: str) -> data_dict:
    with open(file_name, 'r', encoding='utf-8') as file_in:
        students_dict = json.load(file_in, parse_int=int)
    return students_dict


def get_data(students_dict: data_dict) -> list[Student]:
    students_list = []
    for fio, value in students_dict.items():
        try:
            if fio.count(' ') != 2:
                raise ValueError(f'Ошибка в ФИО студента: {fio}')
            last_name, first_name, patronymic = fio.split()
            tmp = Student(last_name, first_name, patronymic)
            tmp.estimations = value['оценка']
            tmp.tests = value['тест']
        except Exception as exc:
            print(f'\033[31m{exc.__class__.__name__}: {exc}\033[0m')
            continue
        students_list.append(tmp)
    return students_list


def main():
    result = get_data(loader(json_data_file))
    for student in result:
        print(student)


if __name__ == '__main__':
    main()
