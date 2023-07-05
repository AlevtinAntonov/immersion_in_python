# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


def work_with_files(num_file, name_file, result_file):
    with(
        open(num_file, 'r', encoding='utf-8') as num_f,
        open(name_file, 'r', encoding='utf-8') as name_f,
        open(result_file, 'w', encoding='utf-8') as res_f
    ):
        num = [s.strip() for s in num_f]
        name = [s.strip() for s in name_f]
        if len(num) > len(name):
            name = name + name[:len(num) - len(name)]
        elif len(num) < len(name):
            num = num + num[:len(name) - len(num)]
        for i in range(len(num)):
            num_1, num_2 = num[i].split('|')
            prod = int(num_1) * float(num_2)
            if prod < 0:
                res_f.write(f'{name[i].lower()} - {-prod}\n')
            elif prod > 0:
                res_f.write(f'{name[i].upper()} - {round(prod)}\n')

# from typing import TextIO
#
#
# def read_by_line(file: TextIO):
#     test = file.readline()
#     if not test:
#         file.seek(0)
#         test = file.readline()
#
#     return test[:-1]
