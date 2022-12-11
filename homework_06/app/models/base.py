from sqlalchemy import Column, Integer

from .database import db


class Base(db.Model):
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)
