#!/usr/bin/python3
'''POST an email'''
import sys
import requests


payload = {'email': sys.argv[2]}
r = requests.post(sys.argv[1], data=payload)

if __name__ == "__main__":
    print(r.text)
