from dataclasses import dataclass


@dataclass
class User:
    name: str
    user_id: int
    level: int = 9


if __name__ == '__main__':
    e1 = User('asd', '1', '5')
    e2 = User('zxc', '3', '3')
    print(e1)
    print(e2)
    print(e1.level > e2.level)
