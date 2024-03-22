#!/usr/bin/python3
"""
A Python file that containing
the class definition of a City.
"""


from model_state import Base
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
    name = Column(String(128), primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'))
