# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import randint, choice

CONSONANTS = 'zyxwvtsrqpnmlkjhgfdcb'
VOWELS = 'aeiouy'
ALL = CONSONANTS + VOWELS


def gen_names(count, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        generated = 0
        while generated < count:
            name_length = randint(4, 7)
            res = '' + choice(ALL).upper()
            for _ in range(1, name_length):
                res = res + choice(ALL)
            if any(c in res for c in VOWELS):
                f.write(f'{res}\n')
                generated += 1
