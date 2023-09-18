#!/usr/bin/python3


"""class square module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Implementation of class square which inherits from
        rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """inherits all the attributes of the super class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        str_square = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                       self.y, self.height)
        return str_square

    def area(self):
        """a function that calculates the area of the Square"""
        return self.height * self.width

    def update(self, *args, **kwargs):
        """
            Args:
                *args (ints):no-keyword arguments which are
                assigned to instance variables in order they arguments
                are arranged during instantiation.
                **kwars (dict): key/value pairs for instance attributes.

        """
        d = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                if i < len(d):
                    setattr(self, d[i], args[i])
        else:
            for kwarg in kwargs:
                if kwarg in d:
                    idx = d.index(f'{kwarg}')
                    setattr(self, d[idx], kwargs[f'{kwarg}'])

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle class"""

        return {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
