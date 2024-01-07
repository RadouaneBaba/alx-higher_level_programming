#!/usr/bin/python3
"""fetch using urllib"""
import urllib.request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        resp = response.read()
        print("Body response:")
        print(f"\t- type: {type(resp)}")
        print(f"\t- content: {resp}")
        print(f"\t- utf8 content: {resp.decode('utf-8')}")
