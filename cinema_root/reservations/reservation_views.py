from .controllers import ReservationController
from ..movies import MovieViews
import os

# DECORATOR log_info?
# import movies, susdavame obekt i t.n


class ReservationViews:
    def __init__(self):
        self.controller = ReservationController()

    def add_reservation(self):
        print('Hello!')
        movies = MovieViews()
        num_of_tickets = input('Please enter number of tickets: ')
        os.system('clear')
        print('Current movies:')
        movies.show_all_movies()
        movie_id = input('Choose a movie: ')
        os.system('clear')
        print('Projections for the movie:')
        # GET PROJECTIONS WITH MOVIE_ID
        projection_id = input('Choose a projection: ')
        os.system('clear')

        # occupied_places = self.controller.get_occupied_seats() <- ТОВА Е ВЕРЕН РЕД, ДОЛНИЯТ ЗА ТЕСТ
        occupied_places = self.controller.get_all_reservations()
        occupied_tuples = []
        for user in occupied_places:
            occupied_tuples.append((user.row, user.col))

        print('Available seats (marked with a dot):')
        print('   1 2 3 4 5 6 7 8 9 10')
        for row in range(10):
            current_row = ''
            for col in range(10):
                if (row, col) in occupied_tuples:
                    if row == 9 and col == 0:
                        current_row += 'X'
                    else:
                        current_row += ' X'
                else:
                    if row == 9 and col == 0:
                        current_row += '.'
                    else:
                        current_row += ' .'
            print(row + 1, current_row)

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var


class AdminReservationView(ReservationViews):
    def __init__(self):
        super().__init__()

    def get_all_reservations(self):
        reservations = self.controller.get_all_reservations()
        for reservation in reservations:
            print('------------------')
            print(f'ID: {reservation.user_id}')
            print(f'Projection_ID: {reservation.projection_id}')
            print(f'Row: {reservation.row}')
            print(f'Col: {reservation.col}')
            print('------------------')
