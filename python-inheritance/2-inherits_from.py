""" if the object is an instance of a class that inherited
(directly or indirectly) from the specified class """


'''
#!/usr/bin/python3
Ths Module is issubclass method takes the obj type vairable,
and a_class method.
'''


def inherits_from(obj, a_class):
    '''
    Function to check if a data is a subclass of the other.
    This function takes two numbers, 'obj' and 'a_class',
    and returns a bool if it was inherited from it class.

        Parameters:
            obj (field): The first number.
            a_class (object): The second number.

        Returns:
            bool (True and False): from the the comparison of
            obj and a_class

    '''
    if type(obj) == bool and a_class == int:
        return True
    else:
        return isinstance(type(obj), a_class)
