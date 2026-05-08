#!/usr/bin/env python3
# Write a function that prints the last digit of a number.

def print_last_digit(number):
	digit = abs (number) %10
	print("{}".format(digit), end="")
	return digit
