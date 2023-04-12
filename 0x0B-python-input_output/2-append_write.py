#!/usr/bin/python3
"""This defines a file-appending function."""


def append_write(filename="", text=""):
    """This appends a string to the end of a UTF8 text file.
    Args:
        filename (str): Is the name of the file to append to.
        text (str): This is the string to append to the file.
    Returns:
        This is the number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
