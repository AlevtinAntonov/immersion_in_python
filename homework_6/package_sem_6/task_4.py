# Задание №4
# � Создайте модуль с функцией внутри.
# � Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# � Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
# Задание №5
# � Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# � Ключ словаря - загадка, значение - список с отгадками.
# Задание №6
# � Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки,
# с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.
__all__ = ['zg_dict', 'out_result']
def zg(text: str, st_answer: set, max_num: int = 5):
    print(text)
    for i in range(1, max_num + 1):
        ans = input(f"Введите ответ попытка {i} ")
        if ans in st_answer:
            zg_result(ans, i)
            return i
    return 0


def zg_dict():
    zg_dict = {
        'Не лает, не кусает, в дом не пускает': ['замок'],
        'Сидит дед во сто шуб одет': ['лук', 'луковица'],
        # 'Что можно увидеть с закрытыми глазами?': ['сон', 'мечту', 'Сон', 'Мечта'],
        # 'Кто его делает, тот не использует, а пользующийся не видит?': ['гроб', "Гроб"],
        # 'Что можно увидеть, но не потрогать?': ['сон', 'мечту', 'отражение'],
        # 'Что идет вверх, но не спускается вниз?': ['возраст', 'Возраст'],
        # 'Кто опирается на четыре ноги, потом на две, а в конце остается на трех?': ['человек'],
        # 'Что можно сломать, не касаясь?': ['обещание'],
        # 'Что имеет ухо, но не слышит?': ['игла', 'Игла'],
        # 'Что можно разбить только одним словом?': ['молчание', 'Молчание', 'Тишина', 'тишина'],
        # 'Что можно увеличить, уменьшить, перевернуть вверх ногами и все равно оно будет оставаться тем же самым?': [
        #     'зеркало', 'Зеркало'],
        # 'Что всегда идет вперед, но никогда не движется?': ['время', 'Время'],
        # 'Что можно купить, но никогда не продать?': ['Знание', 'Информация'],
        # 'Первый, но последний, второй, но первый, третий, но второй': ['Зима', 'Месяцы зимы', 'Зимние месяцы'],
    }
    for qw, ans in zg_dict.items():
        zg(qw, ans)


def zg_result(txt, try_num):
    _global_dict[txt] = try_num


def out_result():
    print('Statistics:\n' + '\n'.join(f'FOR:  {k:<50}' + f'SUCCESS FROM TRY №: {v}' * (v != 0) +
                                      'ALL TRIES UNSUCCESSFUL' * (v == 0) for k, v in _global_dict.items()))


_global_dict = {}
