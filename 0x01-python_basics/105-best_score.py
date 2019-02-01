#!/usr/bin/python3


def best_score(my_dict):
    '''return the key with the biggest value pair in the dict'''

    if type(my_dict) is not dict:
        return
    m = max(my_dict.values())
    for k, v in my_dict.items():
        if v == m:
            return k
