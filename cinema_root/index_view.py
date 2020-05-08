from cinema_root.users.views import UserViews
from .utils import HACKCINEMA
import os

ALL_COMMANDS = ['login', 'signup', 'exit']


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


def input_command():
    command = input('Choose a command:\n[-] login\n[-] signup\n\n[-] exit\n\nInput: ')
    while command not in ALL_COMMANDS:
        os.system('clear')
        print(HACKCINEMA)
        print('Welcome to HackCinema!\n')
        print(f'Your last command ({command}) was not recognized.\n')
        command = input('Choose a command:\n[-] login\n[-] signup\n\n[-] exit\n\nInput: ')
    return command


def print_hackcinema():
    os.system('clear')
    print(HACKCINEMA)
    print('[Welcome to HackCinema!]\n')
