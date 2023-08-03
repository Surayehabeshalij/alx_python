#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry():
    def __getattr__(self, name):
        if name == '__dir__':
            attrs = dir(type(self))
            attrs.remove('__init_subclass__')
            return lambda: attrs
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    __doc__ ="""
    see work
    """
__doc__ = """
pass
"""
