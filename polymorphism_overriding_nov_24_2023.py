# Overriding 
from abc import ABC , abstractmethod
import math


class Shapes:
    def __init__(self, shapename):
        self.shapename = shapename

    @abstractmethod
    def get_area(self):
        pass


class Circle(Shapes):
    def __init__(self, shapename, radius):
        super().__init__(shapename)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
    
class Rectangular(Shapes):
    def __init__(self, shapename, width, height):
        super().__init__(shapename)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    

circle = Circle("Cirlce", 5.0)
rectangular = Rectangular("Rectangular", 4.0, 5.0)

print(f"{circle.shapename}: with radius {circle.radius}")
print(f"{rectangular.shapename}: with width, height {rectangular.width} , {rectangular.height}")

print(circle.get_area())
print(rectangular.get_area())