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
            if not r.get('previous'):
                print("Number of results: {}".format(r.get('count')))
            for result in r.get('results'):
                print(result.get('name'))
                for film in result.get('films'):
                    title = requests.get(film).json().get('title')
                    print("\t{}".format(title))
            r = requests.get(r.get('next'))
        except Exception:
            exit()
