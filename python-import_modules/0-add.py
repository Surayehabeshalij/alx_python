#!/usr/bin/python3
# import the add function from add_0.py
from . import add_0
if __name__ == '__main__':
    
    a = 1
    b = 2
    
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
# print the result of the addition

