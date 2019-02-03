#!/usr/bin/python3


def common_elements(set_1, set_2):
    '''find common elements in two sets'''

    res = []
    for i in set_1:
        if i in set_2:
            res.append(i)
    return res
