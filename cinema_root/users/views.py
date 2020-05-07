from .controllers import UserController
from .admin_view import AdminView
from .client_view import ClientView
from cinema_root.utils import get_input
import getpass
import time
import os


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        for i in range(3):
            email = get_input('Email: ')
            password = getpass.getpass(prompt='Password: ')

            try:
                user = self.controller.login_user(email=email, password=password)

                if user:
                    print('Success!')
                    time.sleep(2)
                    if user.user_type == 'Admin':
                        return AdminView(user)
                    elif user.user_type == 'Client':
                        return ClientView(user)

            except Exception as exc:
                os.system('clear')
                print(str(exc) + '\nTry again!')
        print('You tried to log in 3 times. No more tries!')

    def signup(self):
        user = ''
        while not user:
            email = get_input('Email: ')
            password = get_input('Password: ')

            try:
                user = self.controller.add_user(email=email, password=password)
                return ClientView(user)
            except ValueError as exc:
                print(str(exc) + '\nTry again!')
            except AssertionError as exc:
                print(str(exc) + '\nTry again!')
