#!/usr/bin/env python3
"""
Module that defines a Square class inheriting from Rectangle.
"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
