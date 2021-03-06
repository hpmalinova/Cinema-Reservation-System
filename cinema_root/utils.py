import os


def get_input(msg):
    var = input(msg)
    while not var:
        var = input(msg)
    return var


def input_command():
    ALL_COMMANDS = ['login', 'signup', 'exit']
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


def show_help_exists():
    print(BACKGROUND_LINE)
    print("#  If you don't know what to do, type 'help'")
    print(BACKGROUND_LINE)


HACKCINEMA = r'''
#  -_---_------------_----_____-_----------------------------
#  |-|-|-|----------|-|--/--__-(_)---------------------------
#  |-|_|-|-__-_--___|-|-_|-/--\/_-_-__---___-_-__-___---__-_-
#  |--_--|/-_`-|/-__|-|/-/-|---|-|-'_-\-/-_-\-'_-`-_-\-/-_`-|
#  |-|-|-|-(_|-|-(__|---<|-\__/\-|-|-|-|--__/-|-|-|-|-|-(_|-|
#  \_|-|_/\__,_|\___|_|\_\\____/_|_|-|_|\___|_|-|_|-|_|\__,_|
#  ----------------------------------------------------------
#  ----------------------------------------------------------
'''

BACKGROUND = r'''
#  ----------------------------------------------------------
#  ----------------------------------------------------------
#  ----------------------------------------------------------
#  ----------------------------------------------------------
#  ----------------------------------------------------------
#  ----------------------------------------------------------
#  ----------------------------------------------------------
#  ----------------------------------------------------------
'''

BACKGROUND_LINE = '#  ----------------------------------------------------------'

PREFIX = '#  '

DASH_LENGTH = 59
