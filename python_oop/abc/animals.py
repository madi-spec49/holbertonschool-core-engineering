#!/usr/bin/env python3
"""
Module that defines an abstract class Animal and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.

    This class defines an abstract method 'sound' that must be implemented
    by all subclasses.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that returns the sound the animal makes.

        This method must be implemented by all subclasses.

        Returns:
            str: The sound of the animal
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.

    This class implements the sound method to return "Bark".
    """

    def sound(self):
        """
        Return the sound a dog makes.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.

    This class implements the sound method to return "Meow".
    """

    def sound(self):
        """
        Return the sound a cat makes.

        Returns:
            str: "Meow"
        """
        return "Meow"
