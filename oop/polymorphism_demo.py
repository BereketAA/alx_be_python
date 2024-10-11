import math

class Shape:
    """Base class representing a generic shape."""
    
    def area(self):
        """Method to calculate area. This will be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Class representing a rectangle, derived from Shape."""
    
    def __init__(self, length, width):
        """
        Initialize the rectangle with length and width.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Class representing a circle, derived from Shape."""
    
    def __init__(self, radius):
        """
        Initialize the circle with a radius.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)