#!/usr/bin/python3
'''fetch data from intranet'''
import requests

r = requests.get('https://intranet.hbtn.io/status')

if __name__ == "__main__":
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(r.text), r.text))
