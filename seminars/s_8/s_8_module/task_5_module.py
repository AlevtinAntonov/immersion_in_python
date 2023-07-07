# Напишите функцию, которая ищет json файлы в указанной директории и
# сохраняет их содержимое в виде одноименных pickle файлов.
import json
from pathlib import Path
import pickle


def rename_files(path):
    p = Path(path)
    if p.exists():
        for f in p.iterdir():
            if f.suffix[1:] == 'json':
                with(
                    open(f, 'r', encoding='utf-8') as s,
                    open(f'{f.stem}.pickle', 'wb', encoding='utf-8') as d
                ):
                    file_json = json.load(s)
                    pickle.dump(file_json, d)


if __name__ == '__main__':
    rename_files('out')
