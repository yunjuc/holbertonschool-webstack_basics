#!/usr/bin/python3
'''search API'''
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    payload = {'q': q}
    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        r = r.json()
        if r:
            print("[{}] {}".format(r.get('id'), r.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
