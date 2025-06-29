from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Polygon):
    def __init__(self, base, height):
        self._base = base
        self._height = height

    def area(self):
        return 0.5 * self._base * self._height

class Rectangle(Polygon):
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

shapes = [Triangle(10, 5), Rectangle(8, 4)]
for shape in shapes:
    print("Area:", shape.area())
