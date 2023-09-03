#!/usr/bin/python3
"""An empty class"""


class BaseGeometry:
    """This is an empty class"""
    pass
     """This is an empty class"""
     def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
