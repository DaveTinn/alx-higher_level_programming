#!/usr/bin/python3
"""
Deletes all the State objects with the name containing
the letter 'a' from database hbtn_0e_6_usa.
"""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    # Creates an engine and connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    # Create a Session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query the database to deelete State objects containing letter 'a'
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)

    # Commits the changes
    session.commit()

    # Close the session
    session.close()
