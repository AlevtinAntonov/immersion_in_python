import pytest
from user import User
from project import Project


@pytest.fixture
def get_file(tmp_path):
    f_name = tmp_path / 'test_file.txt'
    with open(f_name, 'w+', encoding='utf-8') as f:
        yield f


@pytest.fixture
def set_data(get_file):
    user = "User(name='Иван', user_id=123, level=1)"
    get_file.write(user)



def test_add_user(get_file, set_data):
    pr_user = Project(set_data)
    pr_user.enter('Иван', 123, 1)
    pr_user.add_user('Алевтин', 1001, 1)
    assert pr_user == ("User(name='Иван', user_id=123, level=1)", "User(name='Алевтин', user_id=1001, level=1")


# def test_first_char(set_char):
#     first = set_char.read(5)
#     assert first == 'ABCD'  # специально провалим тест


if __name__ == '__main__':
    pytest.main(['-v'])
