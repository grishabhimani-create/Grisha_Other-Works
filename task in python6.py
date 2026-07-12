from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


# Child class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


# Child class Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Create objects
circle = Circle(7)
rectangle = Rectangle(10, 5)

# Display areas
print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())
