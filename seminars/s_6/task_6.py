# Задание №6
# � Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки,
# с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.

# print('Statistics:\n' + '\n'.join(f'FOR:  {k:<50}' + f'SUCCESS FROM TRY №: {v}' * (v != 0) +
#        'ALL TRIES UNSUCCESSFUL' * (v == 0) for k, v in my_dict.items()))

_global_dict = {}
