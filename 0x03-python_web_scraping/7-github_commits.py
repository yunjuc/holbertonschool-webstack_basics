#!/usr/bin/python3
'''github API'''
import requests
import sys

url = 'https://api.github.com/repos'
repo = sys.argv[1]
owner = sys.argv[2]

r = requests.get("{}/{}/{}/commits".format(url, repo, owner))
r = r.json()[:10]

if __name__ == "__main__":
    for i in r:
        print("{}: {}".format(i.get('sha'), i.get('commit').get('author')
              .get('name')))
