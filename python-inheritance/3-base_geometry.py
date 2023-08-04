#!/usr/bin/python3
"""BaseGeometry class Module"""


class BaseGeometry():

    def __dir__(self) -> Iterable[str]:
        pass
    def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
    __doc__ ="""
    see work
    """
__doc__ = """
pass
"""
