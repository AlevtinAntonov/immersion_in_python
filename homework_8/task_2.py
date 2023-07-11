# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import csv
import pickle


def read_csv_file(file):
    """
    read csv file without csv.DictReader
    :param file: input csv file
    :return:
    """
    with open(file, 'r',  encoding='utf-8') as f:
        file_reader = csv.reader(f)
        print(pickle.dumps(list(file_reader)))

if __name__ == '__main__':
    read_csv_file('task_1.csv')