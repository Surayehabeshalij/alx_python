#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""
"""
parent class: BaseGeometry
child class: Rectangle
"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """ the class inherite from rectangle """
    def __init__(self, size):
        """use the rectangle methods"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        self.__str__()
        self.area()
