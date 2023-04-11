#!/usr/bin/python3
"""Defines a function to check if an object is an inherited instance of a class."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

