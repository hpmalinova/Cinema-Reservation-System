from cinema_root.db import Database
from .user_queries import (SELECT_ALL_USERS, CREATE_USER, GET_USER_BY_ID, GET_USER_ID,
                           GET_USER_BY_EMAIL, GET_CLIENT_BY_ID, MAKE_ADMIN_BY_ID, DELETE_USER_BY_ID)


class UserGateway:
    def __init__(self):
        self.db = Database()

    def add_user(self, *, email, hashed_password):
        # Create User in DB
        self.db.cursor.execute(CREATE_USER, (email, hashed_password, 'Client'))

        # Get User ID from DB
        self.db.cursor.execute(GET_USER_BY_EMAIL, (email,))
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()

        return raw_user

    def login(self, *, email, hashed_password):
        # Get User from DB
        self.db.cursor.execute(GET_USER_BY_EMAIL, (email,))
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()

        if raw_user:
            if hashed_password == raw_user[2]:
                return raw_user
            else:
                raise ValueError('Wrong password')
        else:
            raise ValueError('User not found.')

    def get_user(self, *, id):
        # Get User DB
        self.db.cursor.execute(GET_USER_BY_ID, (id,))
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()

        if raw_user:
            return raw_user
        else:
            raise ValueError('User not found.')

    def get_all_users(self):
        self.db.cursor.execute(SELECT_ALL_USERS)
        raw_users = self.db.cursor.fetchall()

        self.db.connection.commit()

        return raw_users

    def promote_user(self, *, id, user_type):
        self.db.cursor.execute(GET_CLIENT_BY_ID, (id,))
        raw_user = self.db.cursor.fetchone()

        if raw_user:
            self.db.cursor.execute(MAKE_ADMIN_BY_ID, (user_type, id))
            self.db.connection.commit()
        else:
            raise ValueError('User was not found.')

    def delete_user(self, *, id):
        # Delete User from DB
        self.db.cursor.execute(GET_USER_ID, (id,))
        user_id = self.db.cursor.fetchone()[0]

        if user_id:
            self.db.cursor.execute(DELETE_USER_BY_ID, (id,))
            self.db.connection.commit()
        else:
            raise Exception(f'User with id={id} was not found.')
