#!/usr/bin/python3
def is_same_class(obj, a_class):
    return type(obj) is a_class

class MyClass:
    pass

obj = MyClass()
print(is_same_class(obj, MyClass))  # True
print(is_same_class(obj, int))  # False
print(is_same_class(obj, object))  # True
