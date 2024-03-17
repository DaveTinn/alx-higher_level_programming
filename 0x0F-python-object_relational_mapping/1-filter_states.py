#!/usr/bin/python3
"""
A script that lists all states
with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    #  Creates a connection to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # Creating the cursor object
    cur = db.cursor()

    # Executes the SQL query to retreive state IDs and names starting with N
    cur.execute("SELECT * FROM states WHERE name\
                LIKE BINARY 'N%' ORDER BY id ASC")

    # Retrieves the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
