#!/usr/bin/env python3
"""
Module that defines a Square class with size and position properties.
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

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: The size of the square (default: 0)
            position: The position of the square as a tuple (default: (0, 0))
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value: A tuple of 2 positive integers

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #.

        If size is equal to 0, print an empty line.
        Uses position to add spacing before each line.
        """
        if self.__size == 0:
            print()
        else:
            # Print empty lines for Y position
            for _ in range(self.__position[1]):
                print()
            # Print the square with X position spacing
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            A string with the square drawn using #.
        """
        if self.__size == 0:
            return ""
        result = []
        # Add empty lines for Y position
        for _ in range(self.__position[1]):
            result.append("")
        # Add the square with X position spacing
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
