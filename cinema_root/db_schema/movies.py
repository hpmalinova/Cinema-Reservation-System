from cinema_root.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (Column, Integer, String, REAL,
                        CheckConstraint, UniqueConstraint)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    year = Column(Integer, CheckConstraint('year BETWEEN 2019 and 2022'), nullable=False)
    rating = Column(REAL, CheckConstraint('rating BETWEEN 0 and 10'))
    children = relationship("Projection", passive_deletes=True)  # Important!
    __table_args__ = (
        UniqueConstraint(title, year),
    )

# CREATE_MOVIES = '''
#     CREATE TABLE IF NOT EXISTS movies(
#         id INTEGER PRIMARY KEY,
#         title VARCHAR(30) NOT NULL,
#         year INTEGER NOT NULL CHECK(year BETWEEN 2019 and 2022),
#         rating REAL CHECK(rating BETWEEN 0 and 10),
#         UNIQUE(title, year)
#     );
# '''
