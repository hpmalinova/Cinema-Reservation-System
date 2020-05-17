from .models import UserModel


class UserController:
    def __init__(self):
        self.model = UserModel

    def add_user(self, email, password):
        return self.model.add_user(email=email, password=password)

    def login_user(self, email, password):
        user = self.model.login(email=email, password=password)
        return user if user is not None else False

    def get_all_users(self):
        return self.model.get_all_users()

    def get_user(self, user_id):
        return self.model.get_user(user_id=user_id)

    def promote_user(self, user_id, user_type):
        self.model.promote_user(user_id=user_id, user_type=user_type)

    def delete_user(self, user_id):
        self.model.delete_user(user_id=user_id)
        user = self.model.get_user(user_id=user_id)

        return True if user is None else False
