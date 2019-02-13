#!/usr/bin/python3
'''twitter API'''
import base64
import requests
import sys


if __name__ == "__main__":
    # get auth token
    url_auth = 'https://api.twitter.com/oauth2/token'
    key = sys.argv[1]
    secret = sys.argv[2]
    token = base64.b64encode(bytes(key+':'+secret, 'utf-8')).decode('ascii')
    headers = {'Authorization': 'Basic '+token, 'Content-Type':
               'application/x-www-form-urlencoded;charset=UTF-8'}
    data = {'grant_type': 'client_credentials'}
    r = requests.post(url_auth, headers=headers, data=data)

    # make request to api
    b_token = r.json().get('access_token')
    headers = {'Authorization': 'Bearer '+b_token}
    url_api = 'https://api.twitter.com/1.1/search/tweets.json'
    payload = {'q': sys.argv[3]}
    r = requests.get(url_api, headers=headers, params=payload)
    r = r.json()
    res = r.get('statuses')[:5]
    for t in res:
        print("[{}] {} by {}".format(t.get('id'), t.get('text'),
                                     t.get('user').get('name')))
