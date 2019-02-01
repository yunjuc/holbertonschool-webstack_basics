#!/usr/bin/python3


def add_integer(a, b):
    '''add two int'''

    if isinstance(a, int) is False and isinstance(a, float) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, int) is False and isinstance(b, float) is False:
        raise TypeError("b must be an integer")
    else:
        return int(a)+int(b)
