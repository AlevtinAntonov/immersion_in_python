# Задание №5
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from seminars.s_9.task_2 import deco_guess_number
from seminars.s_9.task_3 import to_json_wrapper
from seminars.s_9.task_4 import counter_wrap


@counter_wrap(2)
@to_json_wrapper
@deco_guess_number
def game(num: int, count: int):
    for i in range(1, count + 1):
        print(f"Попытка номер {i} ")
        user_num = int(input("Введите число от 1 до 100: "))
        if user_num == num:
            return "Вы угадали!"
        elif user_num < num:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")


if __name__ == '__main__':
    print(game(50, 5))
