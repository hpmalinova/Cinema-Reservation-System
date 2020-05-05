# show_movies
# change email
# change password
# make reservations

class ClientView:
    def __init__(self, user):
        self.user = user
        self.welcome()

    def welcome(self):
        print(f'Welcome to HackCinema, {self.user.email}')
        self.execute_command('help')

        command = self.get_input('>> Your command: ')

        while command != 'exit':
            self.execute_command(command)
            command = self.get_input('>> Your command: ')

        print('Goodbye!')

    # @staticmethod
    def execute_command(self, command):
        all_commands = {'help': self.show_commands, 'view profile': self.view_profile}

        if command in all_commands:
            all_commands[command]()
        else:
            print(f'Unknown command: {command}. Try again!')
            return False

    @staticmethod
    def show_commands():
        print('''
    You can do:
        ''')

    def view_profile(self):
        print(self.user.user_id)
        print(self.user.email)
        print(self.user.password)
        print(self.user.user_type)

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var
