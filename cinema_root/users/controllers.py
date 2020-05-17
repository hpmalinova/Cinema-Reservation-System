from .models import UserModel


class UserController:
    def __init__(self):
        self.model = UserModel

    def add_user(self, email, password):
        try:
            user = self.model.add_user(email=email, password=password)
            return user
        except Exception:
            return '[Oops, something went wrong.]\n[Try again!]'

    def login_user(self, email, password):
        try:
            user = self.model.login(email=email, password=password)
            if user:
                return user
            else:
                return '[Wrong username or password.]\n[Try again!]'
        except Exception:
            return '[Oops, something went wrong.]\n[Try again!]'

    def get_user(self, user_id):
        try:
            user = self.model.get_user(user_id=user_id)
            if user:
                return user
            else:
                return f'[There is no user with id={user_id}.]\n[Try again!]'
        except Exception:
            return '[Oops, something went wrong.]\n[Try again!]'

    def get_all_users(self):
        try:
            users = self.model.get_all_users()
            return users
        except Exception:
            return '[Oops, something went wrong.]\n[Try again!]'

    def promote_user(self, user_id, user_type):
        try:
            self.model.promote_user(user_id=user_id, user_type=user_type)
            return f'[User with id = {user_id} is now an Admin!]\n[Congrats!]'
        except Exception:
            return '[Oops, something went wrong.]\n[Try again!]'

    def delete_user(self, user_id):
        try:
            user = self.model.get_user(user_id=user_id)
            if not user:
                return f'[User with id = {user_id} does not exist.]\n'

            self.model.delete_user(user_id=user_id)
            # Check if user still exists in the DB
            user = self.model.get_user(user_id=user_id)
            if not user:
                return f'[User with id = {user_id} was deleted successfully!]\n'
        except Exception:
            return '[Oops, something went wrong.]\n[Try again!]'
