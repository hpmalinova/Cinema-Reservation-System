from cinema_root.users.views import UserViews
import os


def welcome():
    os.system('clear')
    print('Welcome to HackCinema!')
    all_commands = ['login', 'signup', 'exit']
    command = input('Choose a command:\n- login\n- signup\n- exit\nInput: ')
    user_views = UserViews()

    while command not in all_commands:
        os.system('clear')
        print(f'Unknown command {command}.')
        command = input('Choose a command:\n- login\n- signup\n- exit\nInput: ')

    if command == 'login':
        os.system('clear')
        return user_views.login()
    elif command == 'signup':
        os.system('clear')
        return user_views.signup()
    os.system('clear')
