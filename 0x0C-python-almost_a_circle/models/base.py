#!/usr/bin/python3
"""main"""
import json


class Base:
    """Implementation of a Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
            sets the public instance attribute(id) to argument passed
            if the argument is not else assigns the public instance
            to id passed as argument and increments the __nb_objects.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that converts a python data structure object
        into a JSON string.
        representation.
            Args:
                 list_dictionaries (list): a list containing dictionaries.
            Returns:
                json string representation of a python data structure object.
        """
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_ = []
        obj_name = ""
        if list_objs:
            for obj in list_objs:
                obj_name = obj.__class__.__name__
                x = obj.to_dictionary()
                list_.append(x)
        json_string = cls.to_json_string(list_)
        with open(f'{obj_name}.json', "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string == []:
            return []
        else:
            new_list = json_string[:]
            return json.loads(new_list)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)

        return dummy
