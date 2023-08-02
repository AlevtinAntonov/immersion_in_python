# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
import argparse
import logging
from collections import namedtuple
from pathlib import Path

NamedObject = namedtuple('NamedObject', 'name ext is_dir parent', defaults=['', '', False, ''])
FORMAT = "{asctime} - {levelname:<8}: {msg}"

logging.basicConfig(filename='./homework_15/log/log.log',
                    filemode='w',
                    encoding='utf-8',
                    format=FORMAT,
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger()


def parse_ars():
    parser = argparse.ArgumentParser(description="Информация о содержимом директории")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='Введите путь к директорию')
    args = parser.parse_args()
    return args.p


def dir_info(path: str = None):
    if not path:
        logger.info(f'Путь установлен по умолчанию {Path(path)}')
    return directory_traversal(Path().cwd() if path is None else Path(path))


def directory_traversal(file: Path):
    fs_objects = []
    try:
        if file.is_file():
            obj_name = Path(file.name).stem
            obj_ext = Path(file.name).suffix
            obj_dir = False
            fs_objects.append(NamedObject(obj_name, obj_ext, obj_dir, file.parent.name))
            logger.info(f'{obj_name=}| {obj_ext=}| {obj_dir=}| {file.parent.name}')

        else:
            obj_dir = True
            lst_child = []
            for item in file.iterdir():
                child = directory_traversal(item)
                # logger.info(f'{child}')
                lst_child.append(child)

    except Exception as exc:
        print(f'\033[31mERRORR: {exc.__class__.__name__}: {exc}\033[0m')
        logger.info(msg=f'{exc.__class__.__name__}: {exc}')

    return fs_objects


def main():
    for place in parse_ars():
        for item in (dir_info(place)):
            print(repr(item))


if __name__ == '__main__':
    main()

# python .\homework_15\main.py -p ./seminars/s_15
