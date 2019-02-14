#!/usr/bin/python3
'''POST an email'''
import sys
import requests


if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=payload)
    print(r.text)
