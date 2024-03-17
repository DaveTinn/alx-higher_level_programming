#!/usr/bin/python3
"""
A script that prints the State object
with the 'name' passed as an argument from the database hbtn_0e_6_usa.
Results must display the states.id
If no state has the name searched for,
it should display 'Not found'.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":

    """Constructs the database Uniform Resource Identifier (URI)."""
    db_uri = 'mysql+mysqldb://{}:{}:@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3])

    """Creates the SQLAlchemy engine."""
    engine = create_engine(db_uri)

    """Creates the Sesssion factory."""
    Session = sessionmaker(bind=engine)

    """Creats a session."""
    session = Session()

    """
    Queries the state objects with the 'name'
    passed as argument from the database.
    """
    state = session.query(State).filter(State.name == argv[4]).first()

    """Prints the State objects containg 'a'."""
    if state is None:
        print('Not found')
    else:
        print('{}'.format(state.id))
