#!/usr/bin/python3
"""
python file that contains the class definition of a
State and an instance Base = declarative_base()
"""

if __name__ == '__main__':
    from sqlalchemy import Sequence, String, Column, Integer
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           ''.format(sys.argv[1], sys.argv[2],
                                     sys.argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session_maker.configure(bind=engine)
    session = session_maker()
    Base = declarative_base()

    class State(Base):
        __tablename__ = 'states'

        id = Column(Integer, primary_key=True)
        name = Column(String(128))

    Base.metadata.create_all(engine)
