#!/usr/bin/python3
"""
This script defines a function for printing a square using the # character.
"""


def print_square(size):
    """
    Print a square with the # character.

    Args:
        size (int): The height/width of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """

    # Check if size is an integer and is not negative
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
