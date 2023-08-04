#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry
class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def __dir__(self):
        attrs = super().__dir__()
        attrs.remove('__init_subclass__')
        return attrs
