#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry():
     def __dir__(cls):
          attrs = dir(super())
          attrs = dir(type(self))
          attrs = super().__dir__()
          attrs.remove('__init_subclass__')
          return attrs
     __doc__ ="""
    see work
    """
__doc__ = """
pass
"""
