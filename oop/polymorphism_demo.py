import math
class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, length, width, radius):
        super().__init__(length, width)
        self.length = length
        self.width = width
        self.radius = radius 
    def area(self):
        return math.pi * self.radius ** 2
        