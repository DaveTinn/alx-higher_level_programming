#!/usr/bin/python3
"""
A script printing the first State object
from the database hbtn_0e_6_usa.
The state to display must be the first in states.id.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    """Constructs the database URI."""
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3])

    """Creates the SQLAlchemy engine."""
    engine = create_engine(db_uri)

    """Creates a Session factory."""
    Session = sessionmaker(bind=engine)

    """Creates a session."""
    session = Session()

    """Query the first State object, order by states.id."""
    state = session.query(State).order_by(State.id).first()

    """Prints the first State object from the database."""
    if state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(state.id, state.name))
