#!/usr/bin/python3


"""class square module."""

from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size"""
        return self.height

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        str_square = "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                       self.y, self.height)
        return str_square

    def area(self):
        """a function that calculates the area of the Square"""
        return self.height * self.width

    def display(self):
        """Draws the Square on the stdout"""
        for h in range(self.height):
            print("#" * self.width)

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
