

#!/usr/bin/python3
"""Defines an subclass or child list class MyList."""


class MyList(list):
    """This class is a subclass of the built-in list class."""

    def print_sorted(self):
        """This prints a sorted list in an ascending order."""
        print(sorted(self))
