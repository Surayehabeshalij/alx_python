#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry(type):
    """
    documentation
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class ObedClass(metaclass=BaseGeometry):
    """
    documentation for class goes here
    """
    
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

