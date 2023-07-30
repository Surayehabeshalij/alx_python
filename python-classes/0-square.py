class Square:
    def __init__(self, size):
        self.__size = size
    def area(self):
        return self.__size ** 2
    def dict_(self):    
        mysquare = Square(3)
        print(type(mysquare))  # <class 'square.Square'>
        print(mysquare.dict_())  # {'size': 3}
        try:
            print(mysquare._size)
        except Exception as e:
            print(e)                 
