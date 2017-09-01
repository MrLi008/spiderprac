# coding=utf8

from sqlalchemy import Column, String, create_engine, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



# update database models
def updatedatabasemodels():
    class URLData(Base):
        __tablename__ = 'urldata'

        url = Column(String)
        visited = Column(Boolean)

