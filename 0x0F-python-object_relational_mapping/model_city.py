#!/usr/bin/python3
"""contains class definition of a city"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base as StateBase

engine = create_engine('mysql://username:password@localhost/hbtn_0e_0_usa')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class City(Base):
    """describes a class that inherits from base"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


Base.metadata.create_all(engine)
