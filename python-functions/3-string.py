#!/usr/bin/python3
def reverse_string(string):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
#This returns the reversed string
        reversed_string += string[i]
    return reversed_string