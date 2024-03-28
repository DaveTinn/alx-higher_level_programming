#!/usr//bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and,
displays the value of the variable X-Request-Id in the response header.
The packages requests and sys must be used.
"""


from requests import get
from sys import argv

if __name__ == "__main__":
    r = get(argv[1])
    print(r.headers.get('X-Request-Id'))
