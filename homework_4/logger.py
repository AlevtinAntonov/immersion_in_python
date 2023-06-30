from datetime import datetime as dt


def LOG(func):
    def wrapper(*args):
        result = func(*args)
        print(*args)
        with open('log.csv', 'a', encoding='utf-8') as log:
            log.write(
                f'Функция: {func.__name__}; {func.__doc__}; Баланс/Операция № {args}; {dt.now()}\n')
        return result

    return wrapper
