#!/usr/bin/python3
"""contains a file containing class definition of state"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlachemy.orm import sessionmaker

engine = create_engine('mysql://username:password@localhost/hbtn_0e_0_usa')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class State(Base):
    """describes a class that inherits from base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
