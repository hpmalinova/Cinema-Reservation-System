from cinema_root.users.views import UserViews
from .utils import HACKCINEMA
import os


def welcome():
    os.system('clear')
    print(HACKCINEMA)
    print('[Welcome to HackCinema!]\n')
    all_commands = ['login', 'signup', 'exit']
    command = input('Choose a command:\n[-] login\n[-] signup\n\n[-] exit\n\nInput: ')
    user_views = UserViews()

    while command not in all_commands:
        os.system('clear')
        print(HACKCINEMA)
        print('Welcome to HackCinema!\n')
        print(f'Your last command ({command}) was not recognized.\n')
        command = input('Choose a command:\n[-] login\n[-] signup\n\n[-] exit\n\nInput: ')

    if command == 'login':
        os.system('clear')
        return user_views.login()
    elif command == 'signup':
        os.system('clear')
        return user_views.signup()
    os.system('clear')
