#!/usr/bin/python3
def raise_exception_msg(message=""):
    x = raise NameError("Error: {}".format(message))
    return x
try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
