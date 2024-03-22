#!/usr/bin/python3
"""
A script that changes the name of a
State object from the database hbtn_0e_6_usa.
"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """
    Makes sure the code should execute when imported
    as it only executes the code block beneath.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))

    # Creates a Session factory
    Session = sessionmaker(bind=engine)

    # Creates a session
    session = Session()

    # Queries the database for the State_id 2 to be updated
    state_update = session.query(State).filter_by(id=2).first()

    # Update the changes for the
    state_update.name = 'New Mexico'

    # Commits the changes for the State_id 2
    session.commit()

    # Close the session
    session.close()
