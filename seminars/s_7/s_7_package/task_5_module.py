# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import os
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