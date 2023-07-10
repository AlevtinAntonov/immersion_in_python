# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import json
import pickle


def convert_pickle_to_csv(file):
    """
    convert pickle file to csv
    :return:
    """
    with (
        open(file, 'rb') as f,
    open('task_1.csv', 'w', newline='', encoding='utf-8') as c
    ):
        read_file = pickle.load(f)
        print(read_file)
        readheader = csv.DictWriter(c, fieldnames=['Level', 'ID', 'Name', 'Hash'])
        readheader.writeheader()
        readheader.writerows(read_file)

if __name__ == '__main__':
    convert_pickle_to_csv('task_4.pickle')