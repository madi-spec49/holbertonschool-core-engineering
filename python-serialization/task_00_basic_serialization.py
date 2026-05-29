#!/usr/bin/env python3
"""Basic serialization module that serializes a Python dictionary to JSON
and deserializes JSON back to a Python dictionary."""

import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python dictionary to a JSON file.

    Args:
        data (dict): A Python dictionary with data to serialize.
        filename (str): The filename of the output JSON file.
                       If the file already exists, it will be replaced.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Loads and deserializes data from a JSON file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: A Python dictionary with the deserialized JSON data from the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
