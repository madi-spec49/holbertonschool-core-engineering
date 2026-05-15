#!/usr/bin/env python3
"""
Module that defines abstract Shape class and concrete Circle and Rectangle classes.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a geometric shape.

    This class defines abstract methods area and perimeter that must be
    implemented by all subclasses.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.

        Returns:
            float or int: The area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.

        Returns:
            float or int: The perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.

    A circle is defined by its radius.
    """

    def __init__(self, radius):
        """
        Initialize a new Circle instance.

        Args:
            radius (float or int): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Formula: π * r²

        Returns:
            float: The area of the circle
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Formula: 2 * π * r

        Returns:
            float: The perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.

    A rectangle is defined by its width and height.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (float or int): The width of the rectangle
            height (float or int): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Formula: width * height

        Returns:
            float or int: The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Formula: 2 * (width + height)

        Returns:
            float or int: The perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    This function uses duck typing - it doesn't check the type of the object,
    it just calls the area and perimeter methods. Any object that implements
    these methods will work.

    Args:
        shape: Any object that has area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
