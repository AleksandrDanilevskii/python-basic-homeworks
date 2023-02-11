from sqlalchemy import Column, Integer

from .database import db


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
