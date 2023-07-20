#!/usr/bin/python3
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**(1/2))+1):
        if number % i == 0:
            return False
#this will gives as prime numbers for strings
    return True