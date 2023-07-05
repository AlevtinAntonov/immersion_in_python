# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# случайное число от 0 до 255 байтовое представление чмсла
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import os
# from random import randint, choice, randbytes
#
# CONSONANTS = 'zyxwvtsrqpnmlkjhgfdcb'
# VOWELS = 'aeiouy'
# ALL = CONSONANTS + VOWELS
#
#
# def create_file(path, ext, name):
#     with open(f'{path}/{name}/{ext}', 'wb') as f:
#         f.write(randbytes(255))
#
#
# def gen_names(min=6, max=30):
#     while True:
#         name_length = randint(min, max)
#         res = ''
#         for _ in range(name_length):
#             res = res + choice(ALL)
#         if any(c in res for c in VOWELS):
#             return res.capitalize()
# def create(path, min_name=6, max_name=30, count=42, **ext):
#     for k, v in ext.items():
#         for _ in range(v):
#             create_file(path, k, gen_names(min_name, max_name))

import string
from random import choices, randint


def gen_files(ext, min_name_len=6, max_name_len=30, count=42):
    folder_name = 'files'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    for i in range(count):
        file_name = ''.join(choices(string.ascii_lowercase, k=randint(min_name_len, max_name_len)))
        with open(f'{folder_name}/{file_name}.{ext}', 'wb') as f:
            f.write(os.urandom(randint(min_name_len, max_name_len)))
