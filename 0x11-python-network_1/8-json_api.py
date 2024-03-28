#!/usr/bin/python3
"""
Write a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) < 2:
        value = ""
    else:
        value = argv[1]
    payload = {'q': value}
    resp = requests.post(url, data=payload)

    try:
        _dict = resp.json()
        if _dict:
            print("[{}] {}".format(_dict.get('id'), _dict.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
