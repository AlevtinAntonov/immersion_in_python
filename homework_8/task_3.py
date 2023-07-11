# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные
# директории. Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте
# родительскую директорию. Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.
from pathlib import Path
import pickle
import json
import csv

OBJ_CHILD = 'child'
OBJ_PARENT = 'parent'
OBJ_NAME = 'name'
OBJ_TYPE = 'type'
OBJ_TYPE_DIR = 'dir'
OBJ_TYPE_FILE = 'file'
OBJ_SIZE = 'size'


def directory_info(path: str = None):
    return directory_traversal(Path().cwd() if path is None else Path(path))


def directory_traversal(file: Path):
    obj_dict = {OBJ_PARENT: file.parent.name, OBJ_NAME: file.name}
    if file.is_file():
        obj_dict[OBJ_SIZE] = file.stat().st_size
        obj_dict[OBJ_TYPE] = OBJ_TYPE_FILE
    else:
        obj_dict[OBJ_TYPE] = OBJ_TYPE_DIR
        obj_dict[OBJ_SIZE] = 0
        lst_child = []
        for item in file.iterdir():
            child = directory_traversal(item)
            obj_dict[OBJ_SIZE] += child.get(OBJ_SIZE, 0)
            lst_child.append(child)
        obj_dict[OBJ_CHILD] = lst_child

    return obj_dict


def directory_traversal_to_list(res_dict: dict, lst_info: list):
    csv_dict = {
        OBJ_PARENT: res_dict.get(OBJ_PARENT, ''),
        OBJ_NAME: res_dict.get(OBJ_NAME, ''),
        OBJ_TYPE: res_dict.get(OBJ_TYPE, ''),
        OBJ_SIZE: res_dict.get(OBJ_SIZE, 0)
    }
    lst_info.append(csv_dict)
    lst_child = res_dict.get(OBJ_CHILD, None)
    if lst_child is not None:
        for c in lst_child:
            directory_traversal_to_list(c, lst_info)
    return lst_info


def save_to_json(res_dict: dict, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(res_dict, f, indent=2)


def save_to_csv(res_dict: dict, file_name: str):
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=[OBJ_PARENT, OBJ_NAME, OBJ_SIZE, OBJ_TYPE])
        csv_writer.writeheader()
        lst = []
        directory_traversal_to_list(res_dict, lst)
        csv_writer.writerows(lst)


def save_to_pickle(res_dict: dict, file_name: str):
    with open(file_name, 'wb') as f:
        pickle.dump(res_dict, f)


if __name__ == "__main__":
    save_to_json(directory_info('../seminars/s_8'), 'result.json')
    save_to_csv(directory_info('../seminars/s_8'), 'result.csv')
    save_to_pickle(directory_info('../seminars/s_8'), 'result.pickle')
