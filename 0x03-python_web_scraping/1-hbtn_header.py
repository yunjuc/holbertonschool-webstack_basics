#!/usr/bin/python3
'''fetch get request header value'''
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
