from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides
        self.lengths = []

    def get_values(self):
        self.lengths = [float(input(f"Enter length of side {i+1}: ")) for i in range(self.sides)]

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        self.get_values()

    def area(self):
        a, b, c = self.lengths
        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c))**0.5

t = Triangle()
print(f"Area of triangle: {t.area():.2f}")
