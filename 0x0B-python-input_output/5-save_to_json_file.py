#!/usr/bin/python3

"""write object"""
import json


def save_to_json_file(my_obj, filename):
    """writes a JSON object into a textfile."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
