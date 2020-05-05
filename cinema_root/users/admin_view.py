# User
# delete user
# show all users
# show all clients
# change type ? (client-->admin)


# Movie
# add
# delete
# update title/ year
# show all by rating)
# update rating (id)

# Projections
# add
# delete
# update/time/type

from .controllers import UserController


class AdminView:
    def __init__(self, user):
        self.user = user
        self.controller = UserController()
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
        all_commands = {'help': self.show_commands, 'get_all_users': self.get_all_users}

        if command in all_commands:
            all_commands[command]()
        else:
            print(f'Unknown command: {command}. Try again!')
            return False

    def get_all_users(self):
        user_models = self.controller.get_all_users()
        for user in user_models:
            print(user.user_id, user.email, user.password, user.user_type)

    @staticmethod
    def show_commands():
        print('# Users')
        print('- get_user <id>')
        print('- get_all_users')  # DONE
        print('- change_type_user <id> <user_type>')
        print('- delete_user <id>\n')
        print('# Movie')
        print('- add_movie')
        print('- show_all_movies')
        print('- delete_movie\n')
        print('# Projections')
        print('- add_projection')
        print('- update_projection')
        print('- delete_projection')
        print('# help')

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var
