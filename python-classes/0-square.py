#!/usr/bin/python3
class Square:
  def __init__(self, size):
    self.__size = size
    print(Square.area.__doc__)
  def area(self):
        return self.__size ** 2
        