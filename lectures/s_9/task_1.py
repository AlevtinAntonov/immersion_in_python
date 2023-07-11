# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.


def guess_number(num: int, count: int):
    def wrapper():
        for i in range(1, count + 1):
            print(f"Попытка номер {i} ")
            user_num = int(input("Введите число от 1 до 100: "))
            if user_num == num:
                print("Вы угадали!")
                break
            elif user_num < num:
                print("Ваше число меньше")
            else:
                print("Ваше число больше")
    return wrapper


if __name__ == '__main__':
    start_game = guess_number(50, 3)
    start_game()