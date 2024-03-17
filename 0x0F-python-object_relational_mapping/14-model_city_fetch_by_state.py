#!/usr/bin/python3
"""prints all city objects from database hbtn_0e_14_usa"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base as StateBase, State
from model_city import Base as CityBase, City
from sys import argv


def list_cities():
    """takes 3 arguments

    Arguments:
    argv[1]: mysql username
    argv[2]: mysql password
    argv[3]: database name
    """
    engine = create_engine('mysql://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    StateBase.metadata.create_all(engine)
    CityBase.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print(state.name, ':', (city.id), city.name)


if __name__ == "__main__":
    list_cities()
