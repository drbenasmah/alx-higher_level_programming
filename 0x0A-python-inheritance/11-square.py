#!/usr/bin/python3
"""
Defines a Square subclass of Rectangle.
"""

from 9-rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
