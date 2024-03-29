#!/usr/bin/python3
"""
A script taking an argument,
displays all the values in the
table 'states' of a database 'hbtn_0e_0_usa'
where 'name' matches the argument.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    # Creates a connection to MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))

    rows = cur.fetchall()

    for value in rows:
        print(value)

    cur.close()
    db.close()
