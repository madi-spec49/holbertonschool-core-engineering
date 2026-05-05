#!/usr/bin/env python3
import math

# Initialisation de pi avec 2 decimales
Pi_approx = round(math.pi, 2)

# Initialisation du booléen de validation
valid = False
if Pi_approx == 3.14:
    valid = True

print("Language: Python")
print("Version: 3")
print(f"Pi approx: {Pi_approx}")
print(f"Computation valid: {valid}")
