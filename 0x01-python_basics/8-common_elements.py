#!/usr/bin/python3


def common_elements(set_1, set_2):
    '''find common elements in two sets'''

    for i in set_1:
        for j in set_2:
            if i == j:
                return i
    return None
