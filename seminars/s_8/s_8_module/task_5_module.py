# Напишите функцию, которая ищет json файлы в указанной директории и
# сохраняет их содержимое в виде одноименных pickle файлов.
import json
from pathlib import Path
import pickle


def rename_files(path):
    """
    find json files in directory and write to pickle files
    :param path: directiry to find json files
    :return:
    """
    directory = Path(path)
    if directory.exists():
        for file in directory.iterdir():
            if file.suffix == '.json':
                with(
                    open(file, 'r', encoding='utf-8') as s,
                    open(directory / f'{file.stem}.pickle', 'wb') as p
                ):
                    file_json = json.load(s)
                    pickle.dump(file_json, p)


if __name__ == '__main__':
    rename_files('../out')
