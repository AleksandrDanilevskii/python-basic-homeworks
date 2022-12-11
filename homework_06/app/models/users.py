from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, Text

# from .base import Base
from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=False)
    username = Column(String(32), unique=True)
    email = Column(String(64), nullable=False)
    address = Column(Text, nullable=True, default='', server_default='')
    phone = Column(String(32), nullable=True, default='', server_default='')
    website = Column(String(32), nullable=True, default='', server_default='')
    company = Column(String(64), nullable=True, default='', server_default='')

    def __str__(self):
        return f"User(id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email})"

    def __repr__(self):
        return str(self)

    if TYPE_CHECKING:
        query: Query
