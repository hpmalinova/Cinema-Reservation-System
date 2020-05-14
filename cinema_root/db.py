import sqlite3
from .settings import DB_NAME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    REAL,
    CheckConstraint,
    UniqueConstraint,
    ForeignKeyConstraint
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    user_type = Column(String(10), CheckConstraint('user_type = "Admin" or user_type = "Client"'), nullable=False)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    year = Column(Integer, CheckConstraint('year BETWEEN 2019 and 2022'), nullable=False)
    rating = Column(REAL, CheckConstraint('rating BETWEEN 0 and 10'))
    children = relationship("Projection")  # Important!
    __table_args__ = (
        UniqueConstraint(title, year),
    )


class Projection(Base):
    __tablename__ = "projections"
    p_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, nullable=False)
    p_type = Column(String(3), nullable=False)
    p_date = Column(String(10), nullable=False)
    p_time = Column(String(5), nullable=False)
    __table_args__ = (
        UniqueConstraint(p_date, p_time),
        ForeignKeyConstraint(["movie_id"], ["movies.id"], ondelete="CASCADE")
    )


class Reservation(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    projection_id = Column(Integer, nullable=False)
    row = Column(Integer, CheckConstraint('row BETWEEN 1 and 10'), nullable=False)
    col = Column(Integer, CheckConstraint('col BETWEEN 1 and 10'), nullable=False)
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        ForeignKeyConstraint(["projection_id"], ["projections.p_id"], ondelete="CASCADE"),
    )


engine = create_engine(f"sqlite:///{DB_NAME}")
Base.metadata.create_all(engine)


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(DB_NAME)
        self.connection.execute("PRAGMA foreign_keys = 1")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
