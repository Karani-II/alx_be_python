import math
class shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
class rectangle(shape):
    def __init__(self, length, width):
        super().__init__(length, width)
    def area(shape):
        return shape.length * shape.width
class Circle(shape):
    def __init__(self, length, width,radius)
        super().__init__(length, width)
        self.radius = radius 
    def area(self):
        return math.pi * self.radius ** 2
        