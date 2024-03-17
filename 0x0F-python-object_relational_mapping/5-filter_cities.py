#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument,
and lists all cities of that state, using the database hbtn_0e_4_usa.
The script should take 4 arguments.
It must be SQL injection free.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":

    """Creates connection to MySQLdb."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    """ Creates the cursor using a statement and closes the cursor."""
    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        """Retrieves values from the table."""
        values = cur.fetchall()

        """Displays the arguments passed."""
        if values is not None:
            print(", ".join([value[1] for value in values]))

    """Closes the database connection."""
    db.close()
