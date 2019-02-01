#!/usr/bin/python3


def print_diagonal(n):
    '''draw a diagonal'''
    for i in range(n):
        for j in range(i):
            print(' ', end="")
        print('\\')
    print()
