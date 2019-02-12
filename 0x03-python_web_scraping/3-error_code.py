#!/usr/bin/python3
'''display status code'''
import sys
import requests


r = requests.get(sys.argv[1])

if __name__ == "__main__":
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print("Index")
