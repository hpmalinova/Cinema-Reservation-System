from .users_gateway import UserGateway


class UserController:
    def __init__(self):
        self.users_gateway = UserGateway()

    def add_user(self, email, password):
        return self.users_gateway.add_user(email=email, password=password)

    def login_user(self, email, password):
        return self.users_gateway.login(email=email, password=password)

    def get_all_users(self):
        return self.users_gateway.get_all_users()

    def get_user(self, id):
        return self.users_gateway.get_user(id=id)

    def promote_user(self, id, user_type):
        return self.users_gateway.promote_user(id=id, user_type=user_type)

    def delete_user(self, id):
        return self.users_gateway.delete_user(id=id)
