from cinema_root.movies.movie_views import MovieViews
from cinema_root.reservations.reservation_views import ReservationViews
from cinema_root.projections.projection_views import ProjectionView
from cinema_root.utils import get_input

import os


class ClientView:
    def __init__(self, user):
        self.user = user
        self.welcome()

    def welcome(self):
        os.system('clear')
        print(f'Welcome to HackCinema, {self.user.email}')
        self.execute_command('help')

        command = get_input('>> Your command: ')
        os.system('clear')
        while command != 'exit':
            self.execute_command(command)
            input('\nPress Enter')
            os.system('clear')
            print("If you don't know what to do, type 'help'")
            command = get_input('>> Your command: ')
            os.system('clear')

        print('Goodbye!')

    # @staticmethod
    def execute_command(self, command):
        all_commands = {
            'help': self.show_commands, 'view_profile': self.view_profile,
            'show_all_movies': self.show_all_movies,
            'show_projections': self.show_projections,
            'show_projections_by_movie_id': self.show_projections_by_movie_id,
            'make_reservation': self.make_reservation
        }

        command_split = command.split()

        if command_split[0] in all_commands:
            all_commands[command_split[0]](command_split[1:])
        else:
            print(f'Unknown command: {command}. Try again!')

    @staticmethod
    def show_commands(*args):
        print('=============Commands=============')
        print('- view_profile')
        print('- show_all_movies')
        print('- make_reservation')
        print('- show_projections')
        print('- show_projections_by_movie_id <id>')
        print('- help')
        print('- exit')
        print('----------------------------------')

    def view_profile(self, *args):
        print('User ID: ', self.user.id)
        print('Email: ', self.user.email)
        print('Type: ', self.user.user_type)

    def show_all_movies(self, *args):
        MovieViews().show_all_movies()

    def show_projections(self, *args):
        ProjectionView().show_all_projections()

    def show_projections_by_movie_id(self, *args):
        assert args[0] != [], Exception('get_user takes one argument - <id>')
        assert int(args[0][0])
        ProjectionView().show_projections_by_movie_id(int(args[0][0]))

    def make_reservation(self, *args):
        ReservationViews().add_reservation(self.user.id)
