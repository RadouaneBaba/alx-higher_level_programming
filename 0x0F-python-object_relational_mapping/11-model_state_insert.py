#!/usr/bin/python3
"""adds the State object “Louisiana” to the database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    with Session(engine) as session:
        louisiana = State(name="Louisiana")
        session.add(louisiana)
        session.commit()
        print(louisiana.id)
