#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
Use the requests and sys packages only.
"""


import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    status_code = resp.status_code
    if status_code >= 400:
        print('Error code: {}'.format(status_code))
    else:
        print(r.text)
