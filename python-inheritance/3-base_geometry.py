#!/usr/bin/python3
"""BaseGeometry class Module"""


class BaseGeometry(type):

    """
    documentation
    """
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

   
__doc__="""
this documentation
"""
