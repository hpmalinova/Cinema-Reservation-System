from cinema_root.db import Base
# from sqlalchemy.orm import relationship
from sqlalchemy import (Column, Integer, String,
                        CheckConstraint)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    user_type = Column(String(10), CheckConstraint('user_type = "Admin" or user_type = "Client"'), nullable=False)


# CREATE_USERS = '''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY NOT NULL,
#         email VARCHAR(50) UNIQUE NOT NULL,
#         password VARCHAR(50) NOT NULL,
#         user_type VARCHAR(10) NOT NULL CHECK(user_type = 'Admin' or user_type = 'Client')
#     );
# '''
