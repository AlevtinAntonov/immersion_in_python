# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest
from seminars.s_14.task_1 import get_new_text


def test_no_change():
    # возврат строки без изменений
    assert get_new_text('pam pam pam') == 'pam pam pam'


def test_change_register():
    # возврат строки с преобразованием регистра без потери символов
    assert get_new_text('Pam pam Pam') == 'pam pam pam'


def test_delete_sing():
    # возврат строки с удалением знаков пунктуации
    assert get_new_text('pam-pam-pam!...') == 'pampampam'


def test_delete_not_en_symbols():
    # возврат строки с удалением букв других алфавитов
    assert get_new_text('памpamпам') == 'pam'


def test_all_changes():
    # возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
    assert get_new_text('Пам-Pam! PamПарам...') == 'pam pam'


if __name__ == '__main__':
    pytest.main(['-v'])
