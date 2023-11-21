#!/usr/bin/python3
"""
python file that contains the class definition of a
city and an instance Base = declarative_base()
"""

from sqlalchemy import ForeignKey, String, Column, Integer
from model_state import Base


class City(Base):
    """defining the city class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
