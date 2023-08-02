def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
class MyBaseClass:
    pass

class MyClass(MyBaseClass):
    pass

obj = MyClass()
print(is_kind_of_class(obj, MyBaseClass))  # True
print(is_kind_of_class(obj, MyClass))  # True
print(is_kind_of_class(obj, int))  # False
print(is_kind_of_class(obj, object))  # True