#!/usr/bin/env python3
"""Module that defines a Square class with size property."""


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
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value: The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
