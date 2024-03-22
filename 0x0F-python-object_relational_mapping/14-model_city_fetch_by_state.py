#!/usr/bin/python3
"""
A script that prints all City objects
from the database hbtn_0e_14_usa.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":

    """Creates an engine and connects to a MySQL server."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    # Creates a Session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database to print all the City objects
    city_query = session.query(City, State).join(State)

    # Iterate and print the City objects
    for city, state in city_query:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
