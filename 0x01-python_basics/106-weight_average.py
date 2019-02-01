#!/usr/bin/python3


def weight_average(my_list=[]):
    '''return the average a tuple of integers'''

    if len(my_list) is 0:
        return 0

    total = 0.0
    div = 0
    for pair in my_list:
        total += pair[0]*pair[1]
        div += pair[1]
    return total/div
