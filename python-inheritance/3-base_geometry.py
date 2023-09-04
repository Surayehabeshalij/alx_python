""" class: BaseGeometry """
class BaseGeometry(type):
    """ every thing in python is an object soo the class is also an object.
    so if it is an object it have type.type is a metaclass, of which classes
    are instances. Just as an ordinary object is an instance of a class, 
    any new-style class in Python, and thus any class in Python 3, 
    is an instance of the type metaclass """
    def __dir__(cls):
        """ remove the init subclass"""
        attributes = super().__dir__()
        list_to_return = []
        for att in attributes:
            if att != "__init_subclass__":
                list_to_return.append(att)
        return list_to_return

class BaseGeometry(metaclass=BaseGeometry):
    
    """ Metaclasses allow for code to manipulate classes.
    Often this change happens when an object of the class is instantiated
    """

    def __dir__(cls):
        """ remove the init subclass"""
        attributes = super().__dir__()
        list_to_return = []
        for att in attributes:
            if att != "__init_subclass__":
                list_to_return.append(att)
        return list_to_return
