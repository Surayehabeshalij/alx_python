#!/usr/bin/python3
def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
#This will return the values in reverese orders
        for i in range(2, n):
            next_num = fib_seq[i-1] + fib_seq[i-2]
            fib_seq.append(next_num)
        return fib_seq