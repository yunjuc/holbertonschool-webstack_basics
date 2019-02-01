#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    '''print a dict by ordered keys'''

    key = []
    for i in my_dict:
        key.append(i)
    key.sort()
    for k in key:
        print("{}: {}".format(k, my_dict[k]))
