#!/usr/bin/python3
"""changes name of a state object from database hbtn_0e_6_usa"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def change_statename():
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

    update_state = session.query(State).filter(State.id == 2).first()
    if update_state:
        update_state.name = "New Mexico"
        session.commit()


if __name__ == "__main__":
    change_statename()
