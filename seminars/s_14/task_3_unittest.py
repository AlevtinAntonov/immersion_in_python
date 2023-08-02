import unittest
from seminars.s_14.task_1 import get_new_text

class TestUnitGetNewText(unittest.TestCase):
    def test_no_change(self):
        # возврат строки без изменений
        self.assertEqual(get_new_text('pam pam pam'),'pam pam pam')

    def test_change_register(self):
        # возврат строки с преобразованием регистра без потери символов
        self.assertEqual(get_new_text('Pam pam Pam'), 'pam pam pam')

    def test_delete_sing(self):
        # возврат строки с удалением знаков пунктуации
        self.assertEqual(get_new_text('pam-pam-pam!...'), 'pampampam')

    def test_delete_not_en_symbols(self):
        # возврат строки с удалением букв других алфавитов
        self.assertEqual(get_new_text('памpamпам'), 'pam')

    def test_all_changes(self):
        # возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
        self.assertEqual(get_new_text('Пам-Pam! PamПарам...'), 'pam pam')


if __name__ == '__main__':
    unittest.main(verbosity=2)