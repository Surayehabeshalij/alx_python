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
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    __doc__="""
    this is documentation for function
    """