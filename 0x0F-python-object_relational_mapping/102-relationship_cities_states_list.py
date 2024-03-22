#!/usr/bin/python3
"""
A script listing all City objects from the database hbtn_0e_101_usa."""


from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    # Create an engine and establish a connection to MySQLdb server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    # Creates all the table in the database
    Base.metadata.create_all(engine)

    # Creates a Session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database for City objects to be listed
    db_query = session.query(State).join(City).order_by(City.id).all()

    # Prints the result from the query in ascending order
    for state in db_query:
        for city in state.cities:
            print('{}: {} -> {}'.format(city.id, city.name, state.name))

    session.close()
