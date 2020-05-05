from cinema_root.db import Database
from .models import UserModel
from .user_queries import SELECT_ALL_USERS


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def add_user(self, *, email, password):  # DONE
        self.model.validate(email, password)

        hashed_password = self.model.hash_password(password)

        # Create User in DB
        create_query = '''
            INSERT INTO users (email, password, user_type)
            VALUES (?, ?, ?);
        '''
        self.db.cursor.execute(create_query, (email, hashed_password, 'Client'))

        # Get User ID from DB
        get_id_query = f'SELECT id FROM users WHERE email= \'{email}\';'
        self.db.cursor.execute(get_id_query)

        user_id = self.db.cursor.fetchone()[0]

        self.db.connection.commit()

        return self.model(user_id=user_id, email=email,
                          password=hashed_password, user_type='Client')

    def login(self, *, email, password):  # DONE
        # Get User from FB
        get_user_query = f'SELECT * FROM users WHERE email=\'{email}\';'
        self.db.cursor.execute(get_user_query)
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
        get_user_query = f'SELECT * FROM users WHERE id={id};'
        self.db.cursor.execute(get_user_query)
        raw_user = self.db.cursor.fetchone()
        self.db.connection.commit()

        return self.model(raw_user[0], raw_user[1], raw_user[3], raw_user[4])

    def get_all_users(self):  # DONE
        self.db.cursor.execute(SELECT_ALL_USERS)
        raw_users = self.db.cursor.fetchall()

        self.db.connection.commit()

        all_users = []
        for raw_user in raw_users:
            all_users.append(self.model(user_id=raw_user[0], email=raw_user[1],
                                        password=raw_user[2], user_type=raw_user[3]))

        return all_users

    def change_type_user(self, *, id, user_type):  # DONE
        select_user_query = f'SELECT * FROM users WHERE id ={id};'
        self.db.cursor.execute(select_user_query)
        raw_user = self.db.cursor.fetchone()

        if raw_user:
            delete_user_query = f'UPDATE users SET user_type={user_type} WHERE id={id};'
            self.db.cursor.execute(delete_user_query)
            self.db.connection.commit()
        else:
            raise Exception('User not found.')

    def delete_user(self, *, id):
        # Delete User from DB
        select_user_query = f'SELECT * FROM users WHERE id ={id};'
        self.db.cursor.execute(select_user_query)
        raw_user = self.db.cursor.fetchone()

        if raw_user:
            delete_user_query = f'DELETE FROM users WHERE id={id};'
            self.db.cursor.execute(delete_user_query)
            self.db.connection.commit()
        else:
            raise Exception('User not found.')
