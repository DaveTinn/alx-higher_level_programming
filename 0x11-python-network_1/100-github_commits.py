#!/usr/bin/python3
"""
A Python script to solve a technical challenge.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    re = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1]))
    commits = re.json()
    for each_commit in commits[:10]:
        print(each_commit.get('shs'), end=': ')
        print(each_commit.get('commit').get('author').get('name'))
