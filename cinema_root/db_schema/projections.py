from cinema_root.db import Base
from sqlalchemy import (Column, Integer, String,
                        UniqueConstraint, ForeignKeyConstraint)


class Projection(Base):
    __tablename__ = "projections"
    projection_id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, nullable=False)
    projection_type = Column(String(3), nullable=False)
    projection_date = Column(String(10), nullable=False)
    projection_time = Column(String(5), nullable=False)
    __table_args__ = (
        UniqueConstraint(projection_date, projection_time),
        ForeignKeyConstraint(["movie_id"], ["movies.movie_id"], ondelete="CASCADE")
    )


# CREATE_PROJECTIONS = '''
#     CREATE TABLE IF NOT EXISTS projections(
#         p_id INTEGER PRIMARY KEY,
#         movie_id INTEGER NOT NULL,
#         p_type VARCHAR(3) NOT NULL,
#         p_date VARCHAR(10) NOT NULL,
#         p_time VARCHAR(5) NOT NULL,
#         UNIQUE(p_date, p_time),
#         FOREIGN KEY(movie_id) REFERENCES movies(id) ON DELETE CASCADE
#     );
# '''
