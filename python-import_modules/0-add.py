# import the add function from add_0.py
from add_0 import add
if __name__ == '__main__':
    a = 1
    b = 2
    result = add(a, b)
    
# print the result of the addition
print('{} + {} = {}'.format(a, b, add(a, b)))