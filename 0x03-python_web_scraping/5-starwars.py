#!/usr/bin/python3
'''starwar API'''
import requests
import sys

url = 'https://swapi.co/api/people/'
payload = {'search': sys.argv[1]}

r = requests.get(url, params=payload)
r = r.json()

if __name__ == "__main__":
    print("Number of results: {}".format(r.get('count')))
    for i in r.get('results'):
        print(i.get('name'))
