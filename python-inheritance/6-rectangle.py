#!/usr/bin/python3
"""Rectangle class Module"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    def __init__(self, width, height):
        """Initilize rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

        for attr in attributes:
            if attr != "__init_subclass__":
                # append this to the list_to_return
                list_to_return.append(attr)

        return list_to_return
