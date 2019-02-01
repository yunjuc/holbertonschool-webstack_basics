#!/usr/bin/python3


class Square:
    '''square class'''

    def __init__(self, size=0):
        '''constructor'''
        self.size = size

    @property
    def size(self):
        '''size getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''size setter'''
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''area of square'''
        return self.size*self.size

    def my_print(self):
        '''print square'''
        if self.size is 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
