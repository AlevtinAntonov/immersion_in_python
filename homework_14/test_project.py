import pytest
import json
from user import User
from project import Project


# @pytest.fixture
# def get_file(tmp_path):
#     f_name = tmp_path / 'test_file.json'
#     with open(f_name, 'w+', encoding='utf-8') as f:
#         print(f'{f=}')
#         yield f


@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_file.txt'
    print(f'Создаю файл {f_name}')  # принтим в учебных целях
    with open(f_name, 'w+', encoding='utf-8') as f:
        yield f
    print(f'Закрываю файл {f_name}')  # принтим в учебных целях

def set_data(get_file):
    print(f'Заполняю файл {get_file.name} цифрами') # принтим в
    for i in range(10):
        get_file.write('User(name="Иван", user_id=123, level=1)')
    get_file.seek(0)

# @pytest.fixture
# def set_data(get_file):
#     temp = [Project(User(name='Иван', user_id=123, level=1))]
#     return temp


def test_add_user(get_file, set_data):
    pr_user = Project(set_data)
    pr_user.enter('Иван', 123, 1)
    assert pr_user.admin == pr_user


# def test_first_char(set_char):
#     first = set_char.read(5)
#     assert first == 'ABCD'  # специально провалим тест


if __name__ == '__main__':
    pytest.main(['-v'])
