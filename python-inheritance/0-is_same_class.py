#!/usr/bin/python3
def is_same_class(obj, a_class):
    return type(obj) is a_class
class MyClass:
    pass
obj = MyClass()
if is_same_class(obj, int):
    print("{}".format(int.__name__))
if is_same_class(obj, float):
    print("{}".format(float.__name__))
if is_same_class(obj, object):
    print("{}".format(object.__name__))