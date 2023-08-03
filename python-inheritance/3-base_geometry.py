#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry():
    def __init__(self, x):
        self.x = x
    
    def foo(self):
        pass
    
    def __dir__(self):
        # Get the list of attributes and methods
        attrs = dir(type(self))
        # Remove init_subclass from the list
        attrs.remove("init_subclass")
        return attrs
    pass
    __doc__ ="""
    see work
    """
__doc__ = """
pass
"""
