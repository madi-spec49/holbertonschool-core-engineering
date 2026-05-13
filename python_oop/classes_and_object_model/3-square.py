#!/usr/bin/env python3
"""
Defines a class Square.
"""


class Square:
    """
    Represents a square with a private size attribute.
    
    The size attribute is private to enforce encapsulation,
    allowing the class builder to control its type and value.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance.
        
        Args:
        size: The size of the square (private instance attribute)
        """
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.
        
        Returns:
        The area of the square.
        """
        return self.__size ** 2
