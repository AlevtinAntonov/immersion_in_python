# Задание №5
# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса

# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name):
        self.name = name


class Fish(Animal):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def special_info(self):
        return f'Для {self.name} , глубина обитания {self.depth}'


class Bird(Animal):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def special_info(self):
        return f'Для {self.name} , размах крыльев {self.wings}'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def special_info(self):
        return f'Для {self.name} , вес {self.weight}'


if __name__ == '__main__':
    mammal = Mammal('Bob', 4)
    fish = Fish('Neo', 10)
    bird = Bird('Kar', 1)
    print(mammal.special_info())
    print(fish.special_info())
    print(bird.special_info())
