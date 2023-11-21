#!/usr/bin/python3
"""
script that fetches states and their cities
from the database.
using SQLAlchemy module
"""


if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    for state, city in session.query(State, City).filter(
            State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
