#!/usr/bin/python3
"""
A script that lists all State objects,
containing the letter a from the database hbtn_0e_6_usa.
The results must be sorted in ascending order by states.id.
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

    """Queries the state objects that contain letter 'a' in the database."""
    state_filter_a = session.query(State).filter(State.name.contains('a'))

    """Prints the State objects containg 'a'."""
    for state in state_filter_a:
        print('{}: {}'.format(state.id, state.name))
