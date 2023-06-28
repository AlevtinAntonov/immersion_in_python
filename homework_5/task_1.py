# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает
# кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


def path_to_file(abs_path):
    dirname, fname = os.path.split(absolute_path)
    fname, extension = fname.split('.')
    return dirname, fname, extension


def path_to_file_2(abs_path):
    index = abs_path.rfind('/')
    dot = abs_path.rfind('.')
    return abs_path[0:index], abs_path[index + 1:dot], abs_path[dot + 1:]


absolute_path = 'C:/Users/User/Documents/one.txt'
print(path_to_file(absolute_path))
print(path_to_file_2(absolute_path))
