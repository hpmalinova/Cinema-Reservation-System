from cinema_root.db import Database
from .models import UserModel
from .user_queries import SELECT_ALL_USERS


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, email, password):
        self.model.validate(email, password)
        print('email', email)
        hashed_password = self.model.hash_password(password)

        # Create User in DB
        create_query = '''
            INSERT INTO users (email, password, user_type)
            VALUES (?, ?, ?);
        '''
        self.db.cursor.execute(create_query, (email, hashed_password, 'Client'))

        # Get User ID from DB
        get_id_query = f'SELECT id FROM users WHERE email={email};'
        self.db.cursor.execute(get_id_query)

        user_id = self.db.cursor.fetchone()  # CHECK TYPE

        return self.model(user_id, email, hashed_password, 'Client')

    def get_all_users(self):
        self.db.cursor.execute(SELECT_ALL_USERS)
        raw_users = self.db.cursor.fetchall()

        all_users = []
        for raw_user in raw_users:
            all_users.append(self.model(raw_user[0], raw_user[1], raw_user[2], raw_user[3]))

        return all_users

    def get(self, *, email, password):
        # Get User from FB
        get_user_query = f'SELECT * FROM users WHERE email={email};'
        raw_user = self.db.cursor.execute(get_user_query)

        if raw_user:
            hashed_password = self.model.hash_password(password)
            if hashed_password == raw_user[2]:
                return self.model(raw_user[0], raw_user[1], raw_user[2], raw_user[3])
        else:
            raise Exception('User not found.')
