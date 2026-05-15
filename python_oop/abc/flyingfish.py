#!/usr/bin/env python3
"""
Module that demonstrates multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    A class representing a fish.

    Fish live in water and can swim.
    """

    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message indicating where the fish lives."""
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird.

    Birds live in the sky and can fly.
    """

    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message indicating where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish that inherits from both Fish and Bird.

    Flying fish can both swim and fly, and live both in water and the sky.
    This class demonstrates multiple inheritance in Python.
    """

    def fly(self):
        """Override the fly method to describe flying fish soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swim method to describe flying fish swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat method to describe flying fish's unique habitat."""
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    # Create an instance of FlyingFish
    flying_fish = FlyingFish()

    print("=== Method Calls ===")
    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()

    print("\n=== Method Resolution Order (MRO) ===")
    print("MRO using __mro__:")
    for cls in FlyingFish.__mro__:
        print(f"  {cls.__name__}")

    print("\nMRO using mro():")
    for cls in FlyingFish.mro():
        print(f"  {cls.__name__}")
