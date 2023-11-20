class Animal:
    def __init__(self):
        pass

    def make_sound(self, name, sound):
        print(name)
        print(sound)

animal = Animal()
animal.make_sound("cat", "meiwo")

class Dog(Animal):
    def  __init__(self):
        super().__init__()


    def make_sound(self, breed, sound, name):
        print(breed)
        print(sound)
        print(name)

dog = Dog()
dog.make_sound("Dog", "bark", "leef")

class Cat(Animal):
    def  __init__(self):
        super().__init__()


    def make_sound(self, color, sound, name):
        print(color)
        print(sound)
        print(name)

dog = Cat()
dog.make_sound("Cat", "meiwo", "roght")



# second practice




from abc import ABC, abstractmethod
import math


class Shape:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass


class Cirlce(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width  = width

    def get_area(self):
        return self.length * self.width
    

circle_instance  = Cirlce("Cirle", 5.0)
rectangle_instance = Rectangle("Rectangular", 4.0, 6.0)

print(f"{circle_instance.name} with radius {circle_instance.radius}")
print(f"{rectangle_instance.name} with length {rectangle_instance.length} and width {rectangle_instance.width}")

print(f"Area of {circle_instance.name}: {circle_instance.get_area()}")
print(f"Area of {rectangle_instance.name}: {rectangle_instance.get_area()}")
    






        
