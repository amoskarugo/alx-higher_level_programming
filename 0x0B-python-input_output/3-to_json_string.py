#!/usr/bin/python3
"""module to to stringfy using json"""
import json


def to_json_string(my_obj):
    """returns JSON representation of an object."""
    return json.dumps(my_obj)
