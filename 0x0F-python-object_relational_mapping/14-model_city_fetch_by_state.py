#!/usr/bin/python3
"""prints city objects"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import Session

from sqlalchemy import (create_engine, select)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        query = select(City).join(State).order_by(City.id)
        for city in session.scalars(query):
            print(f"{city.state.name}: ({city.id}) {city.name}")
