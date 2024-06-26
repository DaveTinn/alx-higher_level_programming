#!/usr/bin/python3
"""
A script taking in a URL and an email,
sends a POST request to the passed URL with the email as parameter,
and displays the body of the response (decoded in utf-8).
"""


import urllib.request
from sys import argv
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    value = {'email': argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode())
