from cinema_root.movies.movie_views import MovieViews
from cinema_root.reservations.reservation_views import ReservationViews
from cinema_root.projections.projection_views import ProjectionView

import os


class ClientView:
    def __init__(self, user):
        self.user = user
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
        print('- show_projections_by_movie_id')
        print('- help')
        print('----------------------------------')

    def view_profile(self, *args):
        print('User ID: ', self.user.user_id)
        print('Email: ', self.user.email)
        print('Type: ', self.user.user_type)

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var

    def show_all_movies(self, *args):
        MovieViews().show_all_movies()

    def show_projections(self, *args):
        ProjectionView().show_all_projections()

    def show_projections_by_movie_id(self, *args):
        ProjectionView().show_projections_by_movie_id()

    def make_reservation(self, *args):
        ReservationViews().add_reservation()
