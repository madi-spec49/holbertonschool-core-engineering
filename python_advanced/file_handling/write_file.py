#!/usr/bin/env python3
"""Defines a write_file function."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
    return chars_written
