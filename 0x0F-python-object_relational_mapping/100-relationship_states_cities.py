#!/usr/bin/python3
"""
A script that creates the State 'California'
with the City 'San Francisco' from the database hbtn_0e_100_usa.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":

    """Creates an engine and connects to MySQLdb server."""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    # Creates all the tables in the database
    Base.metadata.create_all(engine)

    # Create a Session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Creates the State
    create_state = State(name="California")

    # Creates the City and link it with the State
    create_city = City(name="San Francisco")
    create_state.cities.append(create_city)

    # Add the created State with the City to the session
    session.add(create_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
