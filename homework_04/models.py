"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker, scoped_session, declared_attr, relationship
from sqlalchemy.orm import declarative_base

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


async_engine: AsyncEngine = create_async_engine(url=PG_CONN_URI)
Base = declarative_base(bind=async_engine, cls=Base)

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
# Session = scoped_session(session_factory)


class User(Base):
    name = Column(String(32), unique=False)
    username = Column(String(32), unique=True)
    email = Column(String(32), nullable=False)

    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self):
        return f"User(id={self.id}, name={self.name!r}, username={self.username!r}, email={self.email})"

    def __repr__(self):
        return str(self)


class Post(Base):
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="", server_default="")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="posts", uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, user_id={self.user_id!r}, title={self.title!r})"

    def __repr__(self):
        return str(self)
