#!/usr/bin/python3
"""
A script taking in a URL,
sends a request to the URL and,
displays the value of the X-Request-Id variable
in the header response.
"""


from sys import argv
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
