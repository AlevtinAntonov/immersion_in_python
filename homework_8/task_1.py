# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import json
import pickle


def convert_pickle_to_csv(file, output_file):
    """
    convert pickle file to csv
    :return:
    """
    with (
        open(file, 'rb') as f,
        open(output_file, 'w', newline='', encoding='utf-8') as f2
    ):
        dict_file = pickle.load(f)
        csv_writer = csv.DictWriter(f2, fieldnames=dict_file[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(dict_file)


if __name__ == '__main__':
    convert_pickle_to_csv('task_4.pickle', 'task_1.csv')
