#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in the response"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info().get('X-Request-Id'))
