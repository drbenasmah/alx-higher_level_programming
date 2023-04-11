#!/usr/bin/python3
"""
This line contains the MyList class.
"""


class MyList(list):
    """This line implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """This line print a list in sorted ascending order."""
        print(sorted(self))
