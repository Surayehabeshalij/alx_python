#!/usr/bin/python3
class Square:
  def __init__(self, size):
    self.__size = size
  def area(self):
        return self.__size ** 2
  def perimeter(self):
        return 4 * self.__size
  def __str__(self):
        return f"Square({self.__size})"
