#!/usr/bin/python3


def search_replace(my_list, search, replace):
    '''replace elements in a list and return new list'''

    new = []
    for i in my_list:
        if i == search:
            new.append(replace)
        else:
            new.append(i)
    return new
