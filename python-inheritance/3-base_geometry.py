#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry(type):
    
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
    """
    documentation
    """
__doc__="""
documentation for class 
"""
