class Square:
    def __init__(self, size):
        self.__size = size
    def area (self):
        return self.__size ** 2
    def dict_(self):
        return{'size': self.__size}
print(Square.area.__doc__)
