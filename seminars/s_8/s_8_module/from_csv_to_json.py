# Задание №4
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
import json
def from_csv_to_json(file_csv, file_json):
    """
    read csv file and write to json file
    :param file_csv: in file.csv
    :param file_json: out file.json
    :return:
    """

    with open(file_csv, 'r', encoding='utf-8') as f:
        file = csv.reader(f)
        lst = []
        for i, (level, id_, name) in enumerate(file):
            if i != 0:
                lst.append({
                    'level': int(level),
                    'id_': id_.zfill(10),
                    'name': str(name).title(),
                    'hash': hash(name + id_),
                }
                )
    with open(file_json, 'w', encoding='utf-8') as f2:
        json.dump(lst, f2, indent=2)




