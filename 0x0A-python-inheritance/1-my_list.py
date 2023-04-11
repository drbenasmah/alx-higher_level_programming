#!/usr/bin/python3

class MyList(list):
    """This Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """This Prints out the list in sorted ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
