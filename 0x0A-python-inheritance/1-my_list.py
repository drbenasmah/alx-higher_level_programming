#!/usr/bin/python3

class MyList(list):
    """Inherits from built-in list and implements sorted printing."""

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
