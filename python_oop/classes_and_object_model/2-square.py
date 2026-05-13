#!/usr/bin/env python3
"""Module that defines a Square class with validation."""

class Square:
    """A class that defines a square with a private size attribute.
    
    The size attribute is private to enforce encapsulation,
    allowing the class builder to control its type and value.

    Validations:
        - size must be an integer
        - size must be >= 0
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.
        
        Args:
            size: The size of the square (private instance attribute)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        # Validation du type
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Validation de la valeur
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
