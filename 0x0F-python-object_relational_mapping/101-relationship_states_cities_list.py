#!/usr/bin/python3
"""
A script that list all State objects and corressponding City objects,
contained in the database hbtn_0e_101_usa.
"""


from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    # Creates an engine and connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    # Creates all the tables in the database
    Base.metadata.create_all(engine)

    # Create a Session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database
    db_query = session.query(State).outerjoin(City).order_by(
            State.id, City.id).all()

    # Print the results
    for state in db_query:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))
