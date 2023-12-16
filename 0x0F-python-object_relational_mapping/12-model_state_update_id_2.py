#!/usr/bin/python3
"""adds the State object “Louisiana” to the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine, select)
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    with Session(engine) as session:
        query = select(State).where(State.id == 2)
        state = session.scalars(query).one()
        state.name = "New Mexico"
        session.commit()
