#!/usr/bin/env python3
number = __import__('random').randint(-10000, 10000)

if number < 0:
    lastDigit = -(-number % 10)
else:
    lastDigit = number % 10

if lastDigit == 0:
    print(f"Last digit of {number} is {lastDigit} and is 0")
elif lastDigit > 5:
    print(f"Last digit of {number} is {lastDigit} and is greater than 5")
else:
    print(f"Last digit of {number} is {lastDigit}",
          "and is less than 6 and not 0")
