#!/usr/bin/python3
"""
A script listing all State objects
from the databse hbtn_0e_6_usa,
sorted in ascending order by states.id.
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    """Constructs the database URI."""
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3])

    """Creates an SQLAlchemy engine."""
    engine = create_engine(db_uri)

    """Creates a factory Session."""
    Session = sessionmaker(bind=engine)

    """Creates a session."""
    session = Session()

    """Query all the State objects in order by states.id."""
    states = session.query(State).order_by(State.id)

    # Prints the retrieved state objects
    for state in states:
        print('{}: {}'.format(state.id, state.name))
