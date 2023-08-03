#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry():
     def __dir__(self):
          attrs = dir(type(self))
          attrs.remove('__init_subclass__')
          return attrs
     def __dir__(cls):
        attrs = dir(super())
        attrs.remove('__init_subclass__')
        return attrs
     __doc__ ="""
    see work
    """
__doc__ = """
pass
"""
