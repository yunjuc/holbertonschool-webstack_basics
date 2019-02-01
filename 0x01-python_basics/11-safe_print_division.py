#!/usr/bin/python3


def safe_print_division(a, b):
    '''divide two int and print result'''

    try:
        res = a/b
    except e:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
