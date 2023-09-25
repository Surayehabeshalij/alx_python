#!/usr/bin/python3
"""Defines an inherited class"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited."""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False


""" if the object is an instance of a class that inherited
(directly or indirectly) from the specified class """
