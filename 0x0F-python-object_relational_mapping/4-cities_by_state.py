#!/usr/bin/python3
"""
A script that lists all 'cities',
from the database hbtn_0e_4_usa.
The execute() function is allowed only once.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Creates a connection to the MySQLdb. """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])

    """ Creates a cursor."""
    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)
        """ Retrieves the values in the table. """
        values = cur.fetchall()

        """ Displays the values retrieved. """
        for value in values:
            print(value)
    """ Closes the database connection. """
    db.close()
