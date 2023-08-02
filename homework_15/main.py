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

NamedObject = namedtuple('NamedObject', 'name ext is_dir parent', defaults=['', '', True, ''])
FORMAT = "{asctime} - {levelname:<8}: {msg}"

logging.basicConfig(filename='./homework_15/log/log.txt',
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
    named_objects = []
    try:
        if file.is_file():
            obj_name = Path(file.name).stem
            obj_ext = Path(file.name).suffix
            obj_dir = False
            named_objects.append(NamedObject(obj_name, obj_ext, obj_dir, file.parent.name))
        else:
            for item in file.iterdir():
                child = directory_traversal(item)
                named_objects.append(NamedObject(child))
                logger.info(f'{child}')

    except Exception as exc:
        print(f'\033[31mERROR: {exc.__class__.__name__}: {exc}\033[0m')
        logger.info(msg=f'{exc.__class__.__name__}: {exc}')

    return named_objects


def main():
    for pars_item in parse_ars():
        for item in (dir_info(pars_item)):
            print(repr(item))


if __name__ == '__main__':
    main()

# python3 homework_15/main.py -p ./seminars/s_15
