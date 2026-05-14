#!/usr/bin/env python3
"""
Module that defines a Square class with size property.
"""
class Square:


    """
    A class that defines a square with a private size attribute.
    The size attribute is private to enforce encapsulation,
    allowing the class builder to control its type and value.
    Validations:
        - size must be an integer
        - size must be >= 0
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size of the square (default: 0)
        """
        self.size = size

    @property
    def size(self):
        """Récupère la valeur (retourne une copie, pas la référence)"""
        return self.__size

    @size.setter
    def size(self, value):
        """Valide et assigne la valeur"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
