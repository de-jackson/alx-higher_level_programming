#!/usr/bin/python3
"""defines a class called Square"""


class Square:
    """Represents a class called Squared"""

    def __init__(self, size=0):
        """Initailizes the date
        Args"
            size: size of the square
        """

        self.size = size

    @property
    def size(self):
        """Retrives the size"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size value
        Args:
            value: the size of the sqaure
        """

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >=0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Returns the current sqaure area"""

        return (self.__size * self.__size)
