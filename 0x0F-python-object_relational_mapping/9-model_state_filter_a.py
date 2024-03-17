#!/usr/bin/python3
"""lists state objects containing letter a from database hbtn_0e_6_usa"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def list_astate():
    """takes 3 arguments

    Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    """
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()
    for state in states:
        print(state.id, ':', state.name)


if __name__ == "__main__":
    list_astate()
