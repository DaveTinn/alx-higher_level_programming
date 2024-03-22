#!/usr/bin/python3
"""
A Python file containing
the class definition of a City.
"""


from relationship_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    Defines a class City.

    Attributes:
        id (int): The id (primary key) of the cities
        name (str): Name of the cities in the table.
        state_id (int): The id (Foreign key) of the state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
