#!/usr/bin/python3


class Square:
    '''square class'''

    def __init__(self, size=0, position=(0, 0)):
        '''constructor'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''position getter'''
        return self.__position

    @position.setter
    def position(self, value):
        '''position setter'''
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''area of square'''
        return self.size*self.size

    def my_print(self):
        '''print square'''
        if self.size is 0:
            print()
        else:
            for y in range(self.position[1]):
                print()
            for i in range(self.size):
                for x in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
