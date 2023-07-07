# Задание №3
# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv
import json


def convert_to_csv():
    with (
        open('out/task_2.json', 'r', encoding='utf-8') as f,
        open('out/task_2.csv', 'w', newline='', encoding='utf-8') as c
    ):
        json_read = json.load(f)
        lst = []
        for level, v in json_read.items():
            for id_, name in v.items():
                lst.append(
                    {
                        'level': level, 'id_': id_, 'name': name
                    }
                )
        writer = csv.DictWriter(c, fieldnames=['level', 'id_', 'name'])
        writer.writeheader()
        writer.writerows(lst)


convert_to_csv()
