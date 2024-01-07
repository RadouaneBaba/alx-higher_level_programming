#!/usr/bin/python3
"""fetch using urllib"""
import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        resp = response.read()
        print("Body response:")
        print(f"\t- type: {type(resp)}")
        print(f"\t- content: {resp}")
        print(f"\t- utf8 content: {resp.decode('utf-8')}")
