#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arg=sys.argv
    size= len(arg)-1
# print the number of arguments
if size>1:
    print("{} arguments:".format(size))
    for i in range(size):
        print("{}:{}".format(i+1, arg[i]))
elif size == 0:
    print("{} arguments:".format(size))
else:
    print("{} arguments:".format(size))
    print("{}:{}".format(i, arg[1]))

