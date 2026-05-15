#!/usr/bin/env python3
"""
Module that demonstrates mixins with SwimMixin, FlyMixin, and Dragon classes.
"""


class SwimMixin:
    """
    A mixin class that provides swimming capability.

    Mixins are designed to add specific behaviors to classes.
    This mixin adds the ability to swim.
    """

    def swim(self):
        """Print a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying capability.

    This mixin adds the ability to fly to any class that inherits from it.
    """

    def fly(self):
        """Print a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits from both SwimMixin and FlyMixin.

    Dragons are mythical creatures that can swim, fly, and roar.
    This class demonstrates how mixins can be combined to add multiple
    behaviors without deep inheritance hierarchies.
    """

    def roar(self):
        """Print a message indicating the dragon is roaring."""
        print("The dragon roars!")


if __name__ == "__main__":
    # Create an instance of Dragon
    dragon = Dragon()

    print("=== Dragon Abilities ===\n")
    
    print("Swimming ability:")
    dragon.swim()
    
    print("\nFlying ability:")
    dragon.fly()
    
    print("\nRoaring ability:")
    dragon.roar()
