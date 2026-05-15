#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Module that defines a BaseGeometry class with basic geometric operations.
"""


class BaseGeometry:
    """
    A base class for geometric shapes.

    This class provides foundational functionality that specific geometric
    shape classes will inherit and extend.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method is not implemented in the base class. Subclasses must
        override this method to provide their own area calculation.

        Raises:
            Exception: Always raises an exception indicating the method
                      is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the parameter being validated.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
