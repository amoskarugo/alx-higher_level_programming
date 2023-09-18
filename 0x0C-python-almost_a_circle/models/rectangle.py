#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Implementation of Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor.


        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): The x coordinate of the new rectangle.
            y (y): The y coordinate of the new rectangle.
        Raises:
            TypeError: if the value of height or width is not an integer/
            x or y is not an int
            ValueError: if the value of height or width is  <= 0/
            x or y is less than zero
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.id = id
        super().__init__(id)

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        """getter for private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for private instance attribute x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for private instance attribute y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be  >= 0")
        self.__y = value

    def area(self):
        """a function that calculates the area of the rectangle"""
        return self.__height * self.__width

    def display(self):
        """Draws the rectangle on the stdout"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__width + self.__x):
                if n < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """overrides __str__ method and returns a formatted sting of
            class representation.
        """
        str_format = ("[Rectangle] ({}) {}/{} - "
                      "{}/{}").format(self.id, self.__x, self.__y,
                                      self.__width, self.__height)
        return str_format

    def to_dictionary(self):
        """Returns the dictionary representation of the rectangle class"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

    def update(self, *args, **kwargs):
        """
            Args:
                *args (ints):no-keyword arguments which are
                assigned to instance variables in order they arguments
                are arranged during instantiation.
                **kwars (dict): key/value pairs for instance attributes.

        """
        d = ['id', 'width', 'height',
             'x', 'y']
        if args:
            for i in range(len(args)):
                if i < len(d):
                    setattr(self, d[i], args[i])
        else:
            for kwarg in kwargs:
                if kwarg in d:
                    idx = d.index(f'{kwarg}')
                    setattr(self, d[idx], kwargs[f'{kwarg}'])
