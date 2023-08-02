def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) is not a_class
class MyBaseClass:
    pass

class MyClass(MyBaseClass):
    pass

obj = MyClass()
print(inherits_from(obj, MyBaseClass))  # True
print(inherits_from(obj, MyClass))  # False (obj is an instance of MyClass)
print(inherits_from(obj, int))  # False
print(inherits_from(obj, object))  # True (all classes inherit from object)