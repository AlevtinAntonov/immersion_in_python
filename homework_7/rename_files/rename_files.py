# 1 — Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
from pathlib import Path


def rename_files(new_name, old_extention, path, new_extention):
    p = Path(path)
    if p.exists():
        position = 1
        for f in p.iterdir():
            if f.suffix[1:] == old_extention:
                f.rename(Path(f.parent, f'{f.stem}_{new_name}_{position}.{new_extention}'))
            position += 1


if __name__ == '__main__':
    rename_files('newname', 'pdf', '../misc', 'txt')
