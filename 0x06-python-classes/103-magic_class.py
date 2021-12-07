#!/usr/bin/python3
import math


"""defines a class called MagicClass"""


class MagicClass:
    """Represents a MagicClass"""

    def __init__(self, radius):
        """Initializes the data
        Args:
            radius: radius of magic
        """

        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """Returns the magic area"""

        return self.__radius ** 2 * math.pi

    def circumference(self, radius):
        """Returns the magic circumference"""

        return 2 * math.pi * self.__radius
