#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    '''replace element by position'''

    if idx >= len(my_list):
        return my_list

    new = my_list[:]
    new[idx] = element
    return new
