# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def square(self):
        return self.width * self.length

if __name__ == '__main__':
    a = Rectangle(5)
    b = Rectangle(5, 2)

    print(a.perimeter(), b.perimeter(), a.square(), b.square())
