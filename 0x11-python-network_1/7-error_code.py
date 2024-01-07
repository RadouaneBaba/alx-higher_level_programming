#!/usr/bin/python3
""" handle HTTP errors """
import sys
import requests

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print(f"Error code: {r.status_code}")
