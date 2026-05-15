#!/usr/bin/env python3
"""
Module that defines a Square class inheriting from BaseGeometry.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Square(BaseGeometry):
    """
    A class representing a square that inherits from BaseGeometry.

    The square is defined by its size (side length), which must be a
    positive integer. Validation is performed using the integer_validator
    method from the parent class.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (must be positive integer)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than or equal to 0
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string describing the square with its size
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
