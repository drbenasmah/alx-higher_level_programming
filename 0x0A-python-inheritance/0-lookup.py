#!/usr/bin/python3
"""
This script defines a function called "lookup" which takes an object as input
and returns a list of available attributes and methods of that object.
"""

def lookup(obj):
    """
    This function returns a list of available attributes and methods of an object.
    
    Args:
        obj: An object for which the attributes and methods need to be looked up.
    
    Returns:
        A list of strings containing the names of available attributes and methods of the object.
    """
    return dir(obj)