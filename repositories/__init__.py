from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker

from tables import *

engine = create_engine('postgresql://postgres:98944211@db:5432/FastAPI')
session_maker = sessionmaker(engine)


def create_tables():
    BaseModel.metadata.create_all(engine)
