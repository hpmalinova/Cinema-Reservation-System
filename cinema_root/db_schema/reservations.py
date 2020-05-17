from cinema_root.db import Base
from sqlalchemy import (Column, Integer,
                        CheckConstraint,
                        ForeignKeyConstraint)


class Reservation(Base):
    __tablename__ = "reservations"
    reservation_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    projection_id = Column(Integer, nullable=False)
    row = Column(Integer, CheckConstraint('row BETWEEN 1 and 10'), nullable=False)
    col = Column(Integer, CheckConstraint('col BETWEEN 1 and 10'), nullable=False)
    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.user_id"], ondelete="CASCADE"),
        ForeignKeyConstraint(["projection_id"], ["projections.projection_id"], ondelete="CASCADE"),
    )

# CREATE_RESERVATIONS = '''
#     CREATE TABLE IF NOT EXISTS reservations(
#         id INTEGER PRIMARY KEY,
#         user_id INTEGER NOT NULL,
#         projection_id INTEGER NOT NULL,
#         row INTEGER NOT NULL CHECK(row BETWEEN 1 and 10),
#         col INTEGER NOT NULL CHECK(col BETWEEN 1 and 10),
#         FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
#         FOREIGN KEY(projection_id) REFERENCES projections(p_id) ON DELETE CASCADE
#     );
# '''
