#!/usr/bin/python3
"""Rectangle class Module"""
class BaseGeometry:
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be a positive integer")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
