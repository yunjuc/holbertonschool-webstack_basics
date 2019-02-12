#!/usr/bin/python3
'''fetch get request header value'''
import sys
import requests

r = requests.get(sys.argv[1])

if __name__ == "__main__":
    print(r.headers.get('X-Request-Id'))
