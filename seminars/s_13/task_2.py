# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.
def get_value(my_dict, key, value='key not found'):
    try:
        return my_dict[key]
    except KeyError:
        return value


if __name__ == '__main__':
    grades = {1: 'one', 2: 'two', 3: 'three'}
    print(get_value(grades, 1))
    print(get_value(grades, 3))
    print(get_value(grades, 0))
