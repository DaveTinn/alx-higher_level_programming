#!/usr/bin/python3
"""A script listing all the states from the database hbtn_0e_0_usa."""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")

    row = cur.fetchall()
    for idx in row:
        print(idx)

    cur.close()
    db.close()
