#!/usr/bin/python3
BaseGeometry = __import__('3-base_geometry').BaseGeometry
def __dir__(cls) -> None:
        attributes = super().__dir__()
        return [attribute for attribute in attributes if attribute != '__init_subclass__']
bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))
