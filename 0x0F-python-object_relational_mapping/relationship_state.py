#!/usr/bin/python3
"""
A python file containining the class definition of a State class and
creates an instance declarative_base() named Base.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """
    Represents a class State in the database.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        id (int): The primary key of the state.
        name (str): The name of the state.
        cities: Reperesents a relationship with the class City.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    cities = relationship("City", backref="state", cascade="all, delete")
