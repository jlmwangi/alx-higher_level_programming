#!/usr/bin/python3
"""prints state object with name passed as arg from database hbtn_0e_6_usa"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def list_namestate():
    """takes 3 arguments

    Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    argv[4]: state name to search
    """
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    name = argv[4]

    state = session.query(State).filter(State.name == name).first()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    list_namestate()
