#!/usr/bin/python3
"""
A script taking in a URL and an email,
sends a POST request to the passed URL with the email as parameter,
and displays the body of the response (decoded in utf-8).
"""


import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
