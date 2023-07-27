# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или
# вещественное число. Обрабатывайте не числовые данные как исключения.

def get_number(text: str = None) -> int | float:
    while True:
        try:
            num = float(input(text))
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
        else:
            return int(num) if num.is_integer() else num


if __name__ == '__main__':
    n = get_number('Введите число: ')
    print(f'Результат {n}')
