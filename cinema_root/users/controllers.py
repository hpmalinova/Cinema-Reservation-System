from .models import UserModel


class UserController:
    def __init__(self):
        self.model = UserModel

    def add_user(self, email, password):
        return self.model.add_user(email=email, password=password)

    def login_user(self, email, password):
        return self.model.login(email=email, password=password)

    def get_all_users(self):
        return self.model.get_all_users()

    def get_user(self, id):
        return self.model.get_user(id=id)

    def promote_user(self, id, user_type):
        self.model.promote_user(id=id, user_type=user_type)

    def delete_user(self, id):
        self.model.delete_user(id=id)
