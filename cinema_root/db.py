# import sqlite3
from .settings import DB_NAME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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


class Database:
    engine = create_engine(f"sqlite:///{DB_NAME}")
    Session = sessionmaker(bind=engine)

    @staticmethod
    def create_session():
        return Database.Session()

    @staticmethod
    def create_tables():
        Base.metadata.create_all(Database.engine)

    @staticmethod
    def init_db():
        session = Database.Session()

        session.add_all([
            User(
                email="admin_hackcinema@gmail.com",
                password="17ecee6d6b011925124c7d893d4e88e15a1d2377ebe41132d07bfdceadd273fa",
                user_type="Admin"
            ),
            User(
                email="ivan_petrov@abv.bg",
                password="1b662a97c8895e12a695f08f33442d27e9fe63f62dc4df908439b0a2a789099c",
                user_type="Client"
            ),
            User(
                email="georgi_toshev@yahoo.com",
                password="5f2fb4cbed8d6790efc9ce9f583d6f571e36f73497ed7d0069b2297ab382e019",
                user_type="Client"
            ),
            User(
                email="pesho.petrov@abv.bg",
                password="abba356287d6ce18942a0136b10c6651f47a45a1115a2cbc47e434d9b0475fdc",
                user_type="Client"
            ),
            User(
                email="ludmil.dimitrov@abv.bg",
                password="cabe072d04cfb72f18a9bab9432d41184967dfc3fac386927551a9fd79d7c92b",
                user_type="Client"
            ),
            User(
                email="stefan.n@abv.bg",
                password="5bef7721b8fbcab3f5aabb046e32e2abe37f2851a5b069205ade878f99bbdee8",
                user_type="Client"
            ),
            Movie(
                title="Jojo Rabbit",
                year=2019,
                rating=7.9
            ),
            Movie(
                title="Black Widow",
                year=2020,
                rating=0.0
            ),
            Movie(
                title="Harley Quinn: Birds of Prey",
                year=2020,
                rating=6.2
            ),
            Projection(
                movie_id=1,
                p_type="3D",
                p_date="2020-05-15",
                p_time="19:10"
            ),
            Projection(
                movie_id=1,
                p_type="4DX",
                p_date="2020-05-15",
                p_time="21:00"
            ),
            Projection(
                movie_id=2,
                p_type="4DX",
                p_date="2020-06-15",
                p_time="18:00"
            ),
            Projection(
                movie_id=1,
                p_type="3D",
                p_date="2020-06-15",
                p_time="20:30"
            )
        ])

        session.commit()
        session.close()
