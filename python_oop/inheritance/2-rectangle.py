#!/usr/bin/env python3
"""
Module that defines a Rectangle class inheriting from BaseGeometry.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle that inherits from BaseGeometry.

    The rectangle is defined by its width and height, both of which must be
    positive integers. Validation is performed using the integer_validator
    method from the parent class.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (must be positive integer)
            height (int): The height of the rectangle (must be positive integer)

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is less than or equal to 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: The rectangle description in the format [Rectangle] width/height
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
