#!/usr/bin/env python3
"""
Module that defines a Square class.
"""

class Square:
    """
    A class that defines a square with a private size attribute.
    
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
