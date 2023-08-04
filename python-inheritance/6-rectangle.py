#!/usr/bin/python3
"""Rectangle class Module"""
from importlib import import_module

BaseGeometry = import_module("5-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __dir__(self):
        # Get list of all attributes for this class
        attributes = super().__dir__()

        # Exclude __init_subclass__ from the list
        list_to_return = [attr for attr in attributes if attr != "__init_subclass__"]

        return list_to_return