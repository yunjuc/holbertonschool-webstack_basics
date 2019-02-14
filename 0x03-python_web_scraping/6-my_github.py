#!/usr/bin/python3
'''github API'''
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    r = r.json()
    print(r.get('id'))
