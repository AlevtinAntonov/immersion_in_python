# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
import re
import doctest


def get_new_text(input_text: str):
    """
    >>> get_new_text('pam pam pam')
    'pam pam pam'
    >>> get_new_text('Pam pam Pam')
    'pam pam pam'
    >>> get_new_text('pam-pam-pam!...')
    'pampampam'

    """
    return re.sub(r'[^A-Za-z ]+', '', input_text).lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
