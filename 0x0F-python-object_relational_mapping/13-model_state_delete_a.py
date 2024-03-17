#!/usr/bin/python3
""" deletes all state objects containing letter a from database"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def delete_states():
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

    session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()


if __name__ == "__main__":
    delete_states()
