#!/usr/bin/python3
'''starwar API'''
import requests
import sys

if __name__ == "__main__":
    url = 'https://swapi.co/api/people/'
    payload = {'search': sys.argv[1]}
    r = requests.get(url, params=payload)
    while r:
        try:
            r = r.json()
            print("Number of results: {}".format(r.get('count')))
            for i in r.get('results'):
                print(i.get('name'))
            r = requests.get(r.get('next'))
        except Exception:
            exit()
