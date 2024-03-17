#!/usr/bin/python3
"""prints the first state object from database hbtn_0e_6_usa"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def list_firststate():
    """takes 3 arguments

    Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    """
    engine = create_engine('mysql://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state:
        print(state.id, ':', state.name)
    else:
        print("Nothing", end='')


if __name__ == "__main__":
    list_firststate()
