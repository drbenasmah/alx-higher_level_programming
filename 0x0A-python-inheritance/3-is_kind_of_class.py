#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to or its subclasses.

    Returns:
        bool: True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
