from .controllers import UserController
from .admin_view import AdminView
from .client_view import ClientView


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        for i in range(3):
            email = self.get_input('Email: ')
            password = self.get_input('Password: ')

            try:
                user = self.controller.get_user(email=email, password=password)

                if user:
                    if user.user_type == 'Admin':
                        AdminView(user)
                    elif user.user_type == 'Client':
                        ClientView(user)

            except Exception as exc:
                print(str(exc) + '\nTry again!')
        print('You tried to log in 3 times. No more tries!')
        return

    def signup(self):
        user = ''
        while not user:
            email = self.get_input('Email: ')
            password = self.get_input('Password: ')

            try:
                user = self.controller.create_user(email=email, password=password)
                ClientView(user)
            except ValueError as exc:
                print(str(exc) + '\nTry again!')
            except AssertionError as exc:
                print(str(exc) + '\nTry again!')

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var
