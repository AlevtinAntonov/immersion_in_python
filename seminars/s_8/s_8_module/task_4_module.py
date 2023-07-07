# Задание №4
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
import csv
def from_csv_to_json():

    with open('../out/task_2.csv', 'r', encoding='utf-8') as f:
        file = csv.reader(f)
        lst = []
        for i, (level, id_, name) in enumerate(file):
            dict_json = {}
            if i != 0:
                lst.append({
                    'level': int(level),
                    'id_': id_.zfill(10),
                    'name': str(name).title(),
                    'hash': hash(name + id_)
                }
                )
    print(lst)

from_csv_to_json()

