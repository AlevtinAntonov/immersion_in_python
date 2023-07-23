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

    def _fish_type(self):
        if self.depth <= 10:
            return 'мелководная рыба'
        else:
            return 'глубоководная рыба'

    def special_info(self):
        return f'Для {self.name} , глубина обитания {self.depth} {self._fish_type()}'


class Bird(Animal):
    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def _bird_type(self):
        if self.wings < 1:
            return 'маленькя птичка'
        elif 1 <= self.wings <= 2:
            return 'средняя птичка'
        else:
            return 'крупная птичка'

    def special_info(self):
        return f'Для {self.name} , размах крыльев {self.wings} {self._bird_type()}'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def _mammal_type(self):
        if self.weight < 5:
            return 'маленькое животное'
        elif 5 <= self.weight <= 25:
            return 'среднее животное'
        else:
            return 'крупное животное'

    def special_info(self):
        return f'Для {self.name} , вес {self.weight}, {self._mammal_type()}'


class Dog(Animal):
    pass


if __name__ == '__main__':
    mammal = Mammal('Bob', 4)
    fish = Fish('Neo', 10)
    bird = Bird('Kar', 1)
    print(mammal.special_info())
    print(fish.special_info())
    print(bird.special_info())
