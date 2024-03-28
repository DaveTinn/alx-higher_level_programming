#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status.
No other packages should be imported except 'urllib'.
"""


from urllib import request
with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print('Body response:')
    print("\t - type: {}".format(type(html)))
    print("\t - content: {}".format(html))
    print("\t - utf8 content: {}".format(html.decode('utf-8')))
