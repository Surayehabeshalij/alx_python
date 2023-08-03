#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry():
     def __dir__(cls):
          attrs = dir(type(cls))
          attrs.remove('__init_subclass__')
          return attrs
    
     __doc__ ="""
    see work
    """
__doc__ = """
pass
"""
