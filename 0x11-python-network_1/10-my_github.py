#!/usr/bin/python3
""" display id Github """
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

    print(r.json().get('id'))
