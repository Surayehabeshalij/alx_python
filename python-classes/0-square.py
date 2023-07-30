#!/usr/bin/python3
class Square:
  def __init__(self, size):
    self.__size = size
  def area(self):
        print(Square.area.__doc__)
        return self.__size ** 2
  def perimeter(self):
        return 4 * self.__size
  def __str__(self):
        return f"Square({self.__size})"
  def dict_(self):    
        mysquare = Square(3)
        print(type(mysquare))  # <class 'square.Square'>
        print(mysquare.dict_())  # {'size': 3}
        try:
            print(mysquare._size)
        except Exception as e:
            print(e)  
