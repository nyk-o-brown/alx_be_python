class Shape:
    def area(self):
        """Compute area; subclasses must override this."""
        raise NotImplementedError("Subclasses must implement the area() method")
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of a rectangle."""
        return self.length * self.width
    
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate area of a circle."""
        return math.pi * self.radius ** 2
    