#!/usr/bin/python3


def no_c(str):
    '''remove c and C from a string'''

    new = ""
    for i in str:
        if i != 'c' and i != 'C':
            new += i
    return new
