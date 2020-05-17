from .client_view import ClientView
from .admin_view import AdminView
from .controllers import UserController

from cinema_root.utils import get_input, HACKCINEMA

import getpass
import time
import os


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        for i in range(3):
            email, password = self._get_email_and_password()

            user = self.controller.login_user(email=email, password=password)

            if isinstance(user, str):
                os.system('clear')
                print(user)
            else:
                print('\n#  ------------------------Success!--------------------------')
                time.sleep(1)
                if user.user_type == 'Admin':
                    return AdminView(user)
                elif user.user_type == 'Client':
                    return ClientView(user)

        print('You tried to log in 3 times. No more tries!')

    def signup(self):
        user = ''
        while not user:
            email, password = self._get_email_and_password_with_confirmation()
            user = self.controller.add_user(email=email, password=password)

            if isinstance(user, str):
                os.system('clear')
                print(user)
                user = ''
            else:
                print('\n#  ------------------------Success!--------------------------')
                time.sleep(1)
                return ClientView(user)

    @staticmethod
    def _get_email_and_password():
        print(HACKCINEMA)
        email = get_input('[Email]: ')
        print()
        password = getpass.getpass(prompt='[Password]: ')
        return (email, password)

    def _get_email_and_password_with_confirmation(self):
        email, password = self._get_email_and_password()
        pw_confirm = getpass.getpass(prompt='[Confirm Password]: ')

        while pw_confirm != password:
            os.system('clear')
            print(HACKCINEMA)
            print('[Email]:', email)
            print("\n[Passwords didn't match. Enter password again!]\n")
            password = getpass.getpass(prompt='[Password]: ')
            pw_confirm = getpass.getpass(prompt='[Confirm Password]: ')

        return (email, password)
