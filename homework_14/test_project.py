import pytest
from user import User
from project import Project


@pytest.fixture
def create_users():
    user1 = User('Иван', 123, 1)
    user2 = User(name='Наталья', user_id=741, level=5)
    user3 = User(name='Антон', user_id=456, level=2)
    return [user1, user2, user3]


def test_create_user():
    user = User('Иван', 123, 1)
    assert user.name == 'Иван'
    assert user.user_id == 123
    assert user.level == 1


def test_enter(create_users):
    user = create_users[0]
    with Project(create_users) as p:
        p.enter('Иван', 123, 1)
        assert user.name == 'Иван'
        assert user.user_id == 123
        assert user.level == 1


def test_add_user_not_entered(create_users):
    with Project(create_users) as p:
        p.add_user('Алевтин', 1001, 1)
        assert 'Пользователь не добавлен! Для добавления пользователя войдите в систему.'


def test_add_user_entered(create_users):
    with Project(create_users) as p:
        p.enter('Иван', 123, 1)
        p.add_user('Алевтин', 1002, 2)
        assert create_users[3].name == 'Алевтин'
        assert create_users[3].user_id == 1002
        assert create_users[3].level == 2


def test_del_user(create_users):
    with Project(create_users) as p:
        p.enter('Иван', 123, 1)
        p.enter('Антон', 456, 2)
        p.del_user('Иван', 123, 1)
        assert create_users[0].name != 'Иван'


if __name__ == '__main__':
    pytest.main(['-v'])
