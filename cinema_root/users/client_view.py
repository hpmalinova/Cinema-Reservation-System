from cinema_root.movies.movie_views import MovieViews
from cinema_root.reservations.reservation_views import ReservationViews
from cinema_root.projections.projection_views import ProjectionView
from cinema_root.utils import get_input
from ..utils import BACKGROUND_LINE
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
            input('\n#  Press Enter')
            os.system('clear')
            print(BACKGROUND_LINE)
            print("#  If you don't know what to do, type 'help'")
            print(BACKGROUND_LINE)
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
            'make_reservation': self.make_reservation,
            'show_my_reservations': self.show_my_reservations,
            'delete_reservation': self.delete_reservation
        }

        command_split = command.split()

        if command_split[0] in all_commands:
            all_commands[command_split[0]](command_split[1:])
        else:
            print(f'Unknown command: [{command}]. Try again!')

    @staticmethod
    def show_commands(*args):
        print(BACKGROUND_LINE)
        print('=========================Commands============================')
        print('[-] view_profile\n')
        print('[-] show_all_movies\n')
        print('[-] show_projections')
        print('[-] show_projections_by_movie_id <id>\n')
        print('[-] make_reservation')
        print('[-] show_my_reservations')
        print('[-] delete_reservation\n')
        print('[-] help')
        print('[-] exit')
        print(BACKGROUND_LINE)

    def view_profile(self, *args):
        print(BACKGROUND_LINE)
        print('[User ID]: ', self.user.id)
        print('[Email]:   ', self.user.email)
        print('[Type]:    ', self.user.user_type)
        print(BACKGROUND_LINE)

    def show_all_movies(self, *args):
        MovieViews().show_all_movies()

    def show_projections(self, *args):
        ProjectionView().show_all_projections()

    def show_projections_by_movie_id(self, *args):
        assert args[0] != [], Exception('get_user takes one argument - <id>')
        assert int(args[0][0])
        ProjectionView().show_projections_by_movie_id(int(args[0][0]))

    def show_my_reservations(self, *args):
        ReservationViews().show_my_reservations(self.user.id)

    def make_reservation(self, *args):
        assert args[0] == [], Exception('make_reservation does not take any arguments')
        ReservationViews().add_reservation(self.user.id)

    def delete_reservation(self, *args):
        assert args[0] == [], Exception('delete_reservation does not take any arguments')
        ReservationViews().delete_reservation(self.user.id)
