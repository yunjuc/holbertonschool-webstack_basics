#!/usr/bin/python3


def simple_delete(my_dict, key=""):
    '''delete key from dict'''

    if key in my_dict.keys():
        del my_dict[key]
    return my_dict
