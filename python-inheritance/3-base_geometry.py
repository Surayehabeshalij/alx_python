#!/usr/bin/python3
"""BaseGeometry class Module"""
class BaseGeometry():
     def __init_subclass__(cls):
          pass
    
     def __init__(self, x):
          self.x = x
    
     def foo(self):
          pass
    
     def __dir__(self):
          attrs = super().__dir__()
          attrs.remove('__init_subclass__')
          return attrs

     # Make dir(MyClass) behave the same as dir(MyClass())
     dir = __dir__
     __doc__ ="""
    see work
    """
__doc__ = """
pass
"""
