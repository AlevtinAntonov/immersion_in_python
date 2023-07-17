# Задание №6
# � Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки,
# с которой она угадана).
# � Функция формирует словарь с информацией о результатах отгадывания.
# � Для хранения используйте защищённый словарь уровня модуля.
# � Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# � Для формирования результатов используйте генераторное выражение.

in_dict = {
    'Не лает, не кусает, в дом не пускает': ['замок'],
    # 'Сидит дед во сто шуб одет': ['лук', 'луковица'],
    # 'Что можно увидеть с закрытыми глазами?': ['сон', 'мечту', 'Сон', 'Мечта'],
    # 'Кто его делает, тот не использует, а пользующийся не видит?': ['гроб', "Гроб"],

}


class Riddle:

    def __init__(self, zg_dict: dict, max_num: int = 2):
        self.zg_dict = zg_dict
        self.max_num = max_num

        self.zg()
        self.out_result()

    def zg(self):
        for qw, ans in self.zg_dict.items():
            print(qw)
            for i in range(1, self.max_num + 1):
                answer = input(f"Введите ответ попытка {i} ")
                if answer in ans:
                    self.zg_result(answer, i)
                    return i
            return 0

    def zg_result(self, txt, try_num):
        _global_dict[txt] = try_num

    def out_result(self):
        print('Statistics:\n' + '\n'.join(f'FOR:  {k:<50}' + f'SUCCESS FROM TRY №: {v}' * (v != 0) +
                                          'ALL TRIES UNSUCCESSFUL' * (v == 0) for k, v in _global_dict.items()))


_global_dict = {}

if __name__ == '__main__':
    a = Riddle(in_dict)
