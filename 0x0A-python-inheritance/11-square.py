#!/usr/bin/python3
"""
Defines a Square class based on 9-rectangle.py.
Attributes:
    width (int): Width of the rectangle.
    height (int): Height of the rectangle.
"""

from 9-rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size):
        """Creates new instances of the Square class.
        Args:
            size (int): Size of one side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square.
        Returns:
            str: The square object as a string.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
