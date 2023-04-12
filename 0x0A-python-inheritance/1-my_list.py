#!/usr/bin/python3
"""
Defines a subclass or child list class MyList.
"""


class MyList(list):
    """This class is a subclass of the built-in list class."""

    def print_sorted(self):
        """Print a sorted list in a specific pattern."""
        print(sorted(self))
