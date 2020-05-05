# show_movies
# change email
# change password
# make reservations

class ClientView:
    def __init__(self, user):
        self.user = user
        self.welcome()

    def welcome(self):
        print(f'Welcome to HackCinema, {self.user.name}')
        self.execute_command('help')

        command = self.get_input('>> Your command: ')

        while command != 'exit':
            self.execute_command(command)
            command = self.get_input('>> Your command: ')

        print('Goodbye!')

    # @staticmethod
    def execute_command(self, command):
        all_commands = {'help': self.show_commands}

        if command in all_commands:
            self.execute_command[command]()
        else:
            print(f'Unknown command: {command}. Try again!')
            return False

    @staticmethod
    def show_commands():
        pass

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var
