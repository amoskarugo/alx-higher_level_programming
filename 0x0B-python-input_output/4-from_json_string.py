#!/usr/bin/python3
"""module to convert string to data structure."""
import json


def from_json_string(my_str):
    """converts a JSON string to an object(python data structure)."""
    return json.loads(my_str)
