#!/usr/bin/python3
""" sends post request with param """
import sys
import requests

if __name__ == '__main__':
    let = ''
    if len(sys.argv) == 2:
        let = sys.argv[1]
    try:
        r = requests.post("http://0.0.0.0:5000/search_user", data={'q': let})
        obj = r.json()
        if not obj:
            print("No result")
        else:
            print(f"[{obj.get('id')}] {obj.get('name')}")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
