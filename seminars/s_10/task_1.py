# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def square(cls, area):
        return cls((area / pi) ** 0.5



print(a.circumference(10))
print(a.area())
print(a.square())

