class Square:
    def __init__(self, size):
        self.__size = size    
    def area(self):
        return self.__size ** 2
print(Square.area.__doc__)