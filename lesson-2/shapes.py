import math


class Shape:

    def get_area(self):
        raise ValueError('We don`t know area of some shape')

    def __eq__(self, other):
        return self.get_area() == other.get_area()


class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_area(self):
        return (self.__length * self.__breadth) * 0.5


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_area(self):
        return math.pi * self.__radius ** 2


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.__side = side

    def get_area(self):
        return self.__side * self.__side


rectangle = Rectangle(8, 4)
square = Square(4)
circle = Circle(25)

print(rectangle.__eq__(square))
print(rectangle.__eq__(circle))
