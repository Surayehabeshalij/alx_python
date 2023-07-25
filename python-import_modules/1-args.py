#!/usr/bin/python3
if __name__ == '__main__':
    
    try :
        import sys
        arg = (sys.argv)[1:]
        #arg = input().split()
        size = len(arg)
        if size > 1:
            print("{} arguments:".format(size))
            for i in range(size):
                print("{}: {}".format(i+1, arg[i]))
        elif size == 1:
            print("1 argument:")
            print("1: {}".format(arg[0]))
    except EOFError :
        print("0 arguments.")
    
