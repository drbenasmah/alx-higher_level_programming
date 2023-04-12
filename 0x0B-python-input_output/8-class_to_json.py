#!/usr/bin/python3
"""This defines a Python class-to-JSON function."""


def class_to_json(obj):
    """This returns the dictionary represntation of a simple data structure."""
    return obj.__dict__
