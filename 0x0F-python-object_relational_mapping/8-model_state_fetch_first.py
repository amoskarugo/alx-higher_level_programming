#!/usr/bin/python3
"""
script that fetches the first object in the table
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

    first_obj = session.query(State).order_by(State.id).first()

    if first_obj:
        print("{}: {}".format(first_obj.id, first_obj.name))
    else:
        print("Nothing")
    session.close()
