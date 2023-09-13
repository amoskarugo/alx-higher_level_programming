#!/usr/bin/python3
"""module to convert string to data structure."""


def from_json_string(my_str):
    """converts a JSON string to an object(python data structure)."""
    try:
        json.loads(obj)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
    else:
        return json.loads(obj)
