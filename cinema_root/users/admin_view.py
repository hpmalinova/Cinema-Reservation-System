from .controllers import UserController
from cinema_root.movies.movie_views import AdminMovieView
from cinema_root.projections.projection_views import AdminProjectionView
from cinema_root.reservations.reservation_views import AdminReservationView
from cinema_root.utils import get_input, show_help_exists, BACKGROUND_LINE

import os


class AdminView:
    def __init__(self, user):
        self.user = user
        self.controller = UserController()
        self.welcome()

    def welcome(self):
        os.system('clear')
        print(f'Welcome to HackCinema, \t\t{self.user.email}')
        self.execute_command('help')
        self._get_client_commands()
        print('Goodbye!')

    def execute_command(self, command):
        all_commands = {
            'view_profile': self.view_profile, 'help': self.show_commands,
            'show_all_users': self.show_all_users, 'delete_user': self.delete_user,
            'promote_user': self.promote_user, 'get_user': self.get_user,

            'show_all_movies': self.show_all_movies,
            'add_movie': self.add_movie, 'delete_movie': self.delete_movie,

            'add_projection': self.add_projection, 'delete_projection': self.delete_projection,
            'show_projections': self.show_projections, 'update_projection': self.update_projection,
            'show_projections_by_movie_id': self.show_projections_by_movie_id,

            'show_reservations': self.show_reservations
        }
        command_split = command.split()

        if command_split[0] in all_commands:
            all_commands[command_split[0]](command_split[1:])
        else:
            print(f'Unknown command: [{command}]. Try again!')

    @staticmethod
    def show_commands(*args):
        print(BACKGROUND_LINE)
        print('# Users')
        print('     [-] view_profile')
        print('     [-] get_user <id>')
        print('     [-] show_all_users')
        print('     [-] promote_user <id> <user_type>')
        print('     [-] delete_user <id>\n')
        print('# Movies')
        print('     [-] add_movie')
        print('     [-] show_all_movies')
        print('     [-] delete_movie\n')
        print('# Projections')
        print('     [-] add_projection')
        print('     [-] update_projection')
        print('     [-] delete_projection')
        print('     [-] show_projections')
        print('     [-] show_projections_by_movie_id')
        print(BACKGROUND_LINE)
        print('[|] help')
        print('[|] exit')
        print(BACKGROUND_LINE)

    # User
    def view_profile(self, *args):
        print(BACKGROUND_LINE)
        print('[User ID]: ', self.user.user_id)
        print('[Email]:   ', self.user.email)
        print('[Type]:    ', self.user.user_type)
        print(BACKGROUND_LINE)

    def get_user(self, *args):
        assert args[0] != [], Exception('get_user takes one argument - <id>')
        assert int(args[0][0])

        user_id = int(args[0][0])
        user = self.controller.get_user(user_id=user_id)

        if isinstance(user, str):
            print(user)
        else:
            print(BACKGROUND_LINE)
            print('[User ID]: ', user.user_id)
            print('[Email]:   ', user.email)
            print('[Type]:    ', user.user_type)
            print(BACKGROUND_LINE)

    def show_all_users(self, *args):
        assert args[0] == [], Exception('show_all_users does not take any arguments')

        users = self.controller.get_all_users()

        if not users:
            print('[Currently there are no users]')
        elif isinstance(users, str):
            print(users)
        else:
            print(BACKGROUND_LINE)
            for user in users:
                print('[User ID]: ', user.user_id)
                print('[Email]:   ', user.email)
                print('[Type]:    ', user.user_type)
                print(BACKGROUND_LINE)
            print(BACKGROUND_LINE)

    def promote_user(self, *args):
        assert args[0] != [], Exception('change_type_user takes one argument - <id>')
        assert len(args[0]) == 2, Exception('change_type_user takes two arguments - <id> <user_type>')
        assert args[0][1] == 'Admin', Exception('You can only promote Clients to Admins')
        assert int(args[0][0])

        result = self.controller.promote_user(user_id=int(args[0][0]), user_type=args[0][1])
        print(result)

    def delete_user(self, *args):
        assert args[0] != [], Exception('delete_user takes one argument - <id>')
        assert int(args[0][0])

        result = self.controller.delete_user(user_id=int(args[0][0]))
        print(result)

    # Movie
    def add_movie(self, *args):
        AdminMovieView().add_movie()

    def delete_movie(self, *args):
        AdminMovieView().delete_movie()

    def show_all_movies(self, *args):
        AdminMovieView().show_all_movies()

    # Projection
    def add_projection(self, *args):
        AdminProjectionView().add_projection()

    def delete_projection(self, *args):
        AdminProjectionView().delete_projection()

    def show_projections(self, *args):
        AdminProjectionView().show_all_projections()

    def update_projection(self, *args):
        AdminProjectionView().update_projection()

    def show_projections_by_movie_id(self, *args):
        AdminProjectionView().show_projections_by_movie_id()

    # Reservation
    def show_reservations(self, *args):
        AdminReservationView().show_all_reservations()

    def _get_client_commands(self):
        command = get_input('>> Your command: ')
        os.system('clear')

        while command != 'exit':
            try:
                os.system('clear')
                self.execute_command(command)
                input('\n#  Press Enter')
                os.system('clear')
                show_help_exists()
                command = get_input('>> Your command: ')
                os.system('clear')
            except Exception as exc:
                os.system('clear')
                print(str(exc), '\n')
                show_help_exists()
                command = get_input('>> Your command: ')
