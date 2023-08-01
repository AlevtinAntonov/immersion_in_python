# Задание №2
# На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.
import logging

logging.basicConfig(filename='./logfiles/log_2.log', level=logging.INFO, encoding='utf-8',
                    format='{levelname:<5}, asctime.now(), time:{asctime}, {msg}', style='{'
                    )


def loggernator(func):
    def wrapper(a: int, b: int, c: int):
        res = func(a, b, c)
        logging.info(f'function {func.__name__} was called args {a, b, c} with result {res}')
        return res

    return wrapper


@loggernator
def solving_quadratic_equation(a: int, b: int, c: int):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        x_1 = x_2 = 'None'
    elif a == 0:
        x_1, x_2 = -c / b, 'None'
    elif discriminant == 0:
        x_1, x_2 = -b / 2 * a, 'None'
    else:
        x_1, x_2 = (-b + discriminant ** .5) / (2 * a), (-b - discriminant ** .5) / (2 * a)
    return x_1, x_2


print(solving_quadratic_equation(5, 2, 1))
