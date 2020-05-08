from cinema_root.users.views import UserViews
from .utils import print_hackcinema, input_command
import os


def welcome():
    print_hackcinema()

    user_views = UserViews()

    command = input_command()
    while command != 'exit':
        if command == 'login':
            os.system('clear')
            user_views.login()
        elif command == 'signup':
            os.system('clear')
            user_views.signup()
        print_hackcinema()
        command = input_command()
        os.system('clear')
