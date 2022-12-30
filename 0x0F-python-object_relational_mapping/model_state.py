#!/usr/bin/python3
'''
A python file that contains the class definition of a State and an
instance Base = declarative_base()
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    State class:
    inherits from Base
    links to the MySQL table states
    class attr id that represents a column of an auto-generated,
    unique integer, can't be null aand is a primary key
    class attr name that represents acolumn of a string
    with maximum 128 characters and can't be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
