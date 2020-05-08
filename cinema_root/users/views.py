from .controllers import UserController
from .admin_view import AdminView
from .client_view import ClientView
from cinema_root.utils import get_input
from ..utils import HACKCINEMA
import getpass
import time
import os


class UserViews:
    def __init__(self):
        self.controller = UserController()

    def login(self):
        for i in range(3):
            print(HACKCINEMA)
            email = get_input('[Email]: ')
            print()
            password = getpass.getpass(prompt='[Password]: ')

            try:
                user = self.controller.login_user(email=email, password=password)

                if user:
                    print('\n#  ------------------------Success!--------------------------')
                    time.sleep(1)
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
            print(HACKCINEMA)
            email = get_input('[Email]: ')
            pw_confirm = ''
            print()
            password = getpass.getpass(prompt='[Password]: ')
            pw_confirm = getpass.getpass(prompt='[Confirm Password]: ')

            while pw_confirm != password:
                os.system('clear')
                print(HACKCINEMA)
                print('[Email]:', email)
                print("[Passwords didn't match. Enter password again!]")
                password = getpass.getpass(prompt='[Password]: ')
                pw_confirm = getpass.getpass(prompt='[Confirm Password]: ')
            try:
                user = self.controller.add_user(email=email, password=password)
                print('\n#  ------------------------Success!--------------------------')
                time.sleep(1)
                return ClientView(user)
            except ValueError as exc:
                os.system('clear')
                print(str(exc) + '\nTry again!')
            except AssertionError as exc:
                os.system('clear')
                print(str(exc) + '\nTry again!')
