#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database
using SQLAlchemy module
"""

if __name__ == '__main__':
    from model_state import Base, State
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

    session.add(State(name="Louisiana"))
    session.commit()
    for state in session.query(State).all():
        if state.name == 'Louisiana':
            print("{}".format(state.id))
            break
