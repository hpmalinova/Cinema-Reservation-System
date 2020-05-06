from .controllers import UserController
from cinema_root.movies.movie_views import AdminMovieView
import os


class AdminView:
    def __init__(self, user):
        self.user = user
        self.controller = UserController()
        self.welcome()

    def welcome(self):
        os.system('clear')
        print(f'Welcome to HackCinema, {self.user.email}')
        self.execute_command('help')

        command = self.get_input('>> Your command: ')
        os.system('clear')
        while command != 'exit':
            self.execute_command(command)
            input('\nPress Enter')
            os.system('clear')
            command = self.get_input('>> Your command: ')
            os.system('clear')

        print('Goodbye!')

    # @staticmethod
    def execute_command(self, command):
        all_commands = {
            'help': self.show_commands, 'get_all_users': self.get_all_users, 'delete_user': self.delete_user,
            'promote_user': self.promote_user, 'get_user': self.get_user, 'show_all_movies': self.show_all_movies,
            'add_movie': self.add_movie, 'delete_movie': self.delete_movie
        }
        command_split = command.split()

        if command_split[0] in all_commands:
            all_commands[command_split[0]](command_split[1:])
        else:
            print(f'Unknown command: {command}. Try again!')
            return False

    def get_user(self, *args):
        assert args[0] != [], Exception('get_user takes one argument - <id>')
        assert int(args[0][0])

        user = self.controller.get_user(id=int(args[0][0]))
        print(user.user_id, user.email, user.password, user.user_type)

    def get_all_users(self, *args):
        assert args[0] == [], Exception('get_all_users does not take any arguments')

        user_models = self.controller.get_all_users()

        for user in user_models:
            print(user.user_id, user.email, user.password, user.user_type)

    def promote_user(self, *args):
        assert args[0] != [], Exception('change_type_user takes one argument - <id>')
        assert len(args[0]) == 2, Exception('change_type_user takes two arguments - <id> <user_type>')
        assert args[0][1] == 'Admin', Exception('You can only promote Clients to Admins')
        assert int(args[0][0])

        self.controller.promote_user(id=int(args[0][0]), user_type=args[0][1])

        print(f'User with id = {args[0][0]} is now an Admin!\nCongrats!')

    def delete_user(self, *args):
        assert args[0] != [], Exception('delete_user takes one argument - <id>')
        assert int(args[0][0])

        self.controller.delete_user(id=int(args[0][0]))

        print(f'User with id = {args[0][0]} deleted successfully!')

    @staticmethod
    def show_commands(*args):
        print('# Users')
        print('- get_user <id>')  # DONE
        print('- get_all_users')  # DONE
        print('- promote_user <id> <user_type>')  # DONE
        print('- delete_user <id>\n')  # DONE
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

    def add_movie(self, *args):
        try:
            AdminMovieView().add_movie()
        except ValueError as exc:
            print(str(exc) + '\nTry again.')

    def delete_movie(self, *args):
        AdminMovieView().delete_movie()

    def show_all_movies(self, *args):
        AdminMovieView().show_all_movies()
