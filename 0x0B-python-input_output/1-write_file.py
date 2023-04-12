#!/usr/bin/python3
"""This defines a file-writing function."""


def write_file(filename="", text=""):
    """this writes a string to a UTF8 text file.
    Args:
        filename (str): Is the name of the file to write.
        text (str): Is the text to write to the file.
    Returns:
        This returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
