#!/usr/bin/env python3
# This script generates a random integer between -10 and 10, and prints whether it is positive, negative, or zero.
number = __import__('random').randint(-10, 10)

if number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is negative")
