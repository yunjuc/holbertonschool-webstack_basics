#!/usr/bin/python3


def islower(c):
    '''check if a character is lower case letter'''

    if ord('a') <= ord(c) <= ord('z'):
        return True
    else:
        return False
