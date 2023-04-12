#!/usr/bin/python3
"""
Contains the MyList class.
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Prints out a list in sorted ascending order."""
        print(sorted(self))
