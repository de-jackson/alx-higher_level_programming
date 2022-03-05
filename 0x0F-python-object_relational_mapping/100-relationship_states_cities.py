#!/usr/bin/python3
"""
a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa:
(100-relationship_states_cities.py)
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="California")
    newState.cities = [City(name="San Francisco")]
    session.add(newState)
    session.commit()
    session.close()
