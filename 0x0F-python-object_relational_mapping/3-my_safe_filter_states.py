#!/usr/bin/python3
"""
A script that takes in arguments and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
It should be safe from MySQL injections.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Creates a connection to MySQLdb
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    # Creates a cursor to execute the query
    with db.cursor() as cur:
        # Executes the query
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, {
            'name': argv[4]
        })

    # Retrieves the values in the table
    values = cur.fetchall()

    # Displays the values retrieved
    if values is None:
        for value in values:
            print(value)

    # Close the database and cursor connection
    db.close()
    cur.close()
