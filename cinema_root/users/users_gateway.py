from cinema_root.db import Database
from .models import UserModel
from .user_queries import (SELECT_ALL_USERS, CREATE_USER, GET_USER_ID, GET_USER_BY_ID,
                           GET_USER_BY_EMAIL, GET_CLIENT_BY_ID, MAKE_ADMIN_BY_ID, DELETE_USER_BY_ID)


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def add_user(self, *, email, password):  # DONE
        self.model.validate(email, password)

        hashed_password = self.model.hash_password(password)

        # Create User in DB
        self.db.cursor.execute(CREATE_USER, (email, hashed_password, 'Client'))

        # Get User ID from DB
        self.db.cursor.execute(GET_USER_ID, (email))
        user_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()

        return self.model(user_id=user_id, email=email,
                          password=hashed_password, user_type='Client')

    def login(self, *, email, password):  # DONE
        # Get User from DB
        self.db.cursor.execute(GET_USER_BY_EMAIL, (email))
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()

        if raw_user:
            hashed_password = self.model.hash_password(password)
            if hashed_password == raw_user[2]:
                return self.model(user_id=raw_user[0], email=raw_user[1],
                                  password=raw_user[2], user_type=raw_user[3])
            else:
                raise ValueError('Wrong password')
        else:
            raise ValueError('User not found.')

    def get_user(self, *, id):  # DONE
        # Get User DB
        self.db.cursor.execute(GET_USER_BY_ID, (id))
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()

        if raw_user:
            return self.model(user_id=raw_user[0], email=raw_user[1], password=raw_user[2], user_type=raw_user[3])
        else:
            raise ValueError('User not found.')

    def get_all_users(self):  # DONE
        self.db.cursor.execute(SELECT_ALL_USERS)
        raw_users = self.db.cursor.fetchall()

        self.db.connection.commit()

        all_users = []
        for raw_user in raw_users:
            all_users.append(self.model(user_id=raw_user[0], email=raw_user[1],
                                        password=raw_user[2], user_type=raw_user[3]))

        return all_users

    def promote_user(self, *, id, user_type):  # DONE
        self.db.cursor.execute(GET_CLIENT_BY_ID, (id))
        raw_user = self.db.cursor.fetchone()

        if raw_user:
            self.db.cursor.execute(MAKE_ADMIN_BY_ID, (user_type, id))
            self.db.connection.commit()
        else:
            raise ValueError('User not found.')

    def delete_user(self, *, id):
        # Delete User from DB
        self.db.cursor.execute(GET_USER_BY_ID, (id))
        raw_user = self.db.cursor.fetchone()

        if raw_user:
            self.db.cursor.execute(DELETE_USER_BY_ID, (id))
            self.db.connection.commit()
        else:
            raise Exception('User not found.')
