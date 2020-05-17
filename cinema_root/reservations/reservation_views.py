from .controllers import ReservationController
from cinema_root.movies import MovieViews
from cinema_root.projections import ProjectionView
from cinema_root.utils import get_input, BACKGROUND_LINE
from .validation import validate_row, validate_col

import os


class ReservationViews:
    def __init__(self):
        self.controller = ReservationController()

    def add_reservation(self, user_id):
        reservation_info = self._get_reservation_info()
        num_of_tickets = reservation_info[0]
        movie_id = reservation_info[1]
        projection_id = reservation_info[2]

        occupied_places = self.controller.get_occupied_seats(projection_id)
        occupied_tuples = []
        for user in occupied_places:
            occupied_tuples.append((user.row, user.col))

        self._print_movie_theater(occupied_tuples)

        seats = self._reserve_seats(occupied_tuples, num_of_tickets)

        reserved_seats = ''
        for seat in seats:
            reserved_seats += f'{seat} '

        confirmed = self._confirmation(movie_id, projection_id, reserved_seats)
        print(BACKGROUND_LINE)
        if confirmed:
            for seat in seats:
                self.controller.add_reservation(user_id, projection_id, seat[0], seat[1])
            print('\n#  -----------------------Thank you!-------------------------')
        else:
            print('\n#  ---------Reservation [NOT] confirmed. Going back.---------')
        print(BACKGROUND_LINE)

    def delete_reservation(self, user_id):
        print(BACKGROUND_LINE)
        print('[Hello!]')
        reservation_id = get_input('[Please enter reservation id]: ')
        if self.controller.delete_reservation(int(user_id), int(reservation_id)):
            print(f'[Reservation with id={reservation_id} was successfully deleted.]')
        else:
            print(f'[Oops, something went wrong.\nReservation with id={reservation_id} was not deleted.]')

    def show_my_reservations(self, user_id):
        reservations = self.controller.get_my_reservations(user_id)
        if not reservations:
            print('You have no reservations.')
        for reservation in reservations:
            print(BACKGROUND_LINE)
            print(f'[Reservation_ID]: {reservation.id}')
            print(f'[Projection_ID]:  {reservation.projection_id}')
            print(f'[Row]:            {reservation.row}')
            print(f'[Col]:            {reservation.col}')

    def _get_reservation_info(self):
        print(BACKGROUND_LINE)
        print('[Hello!]')
        movie_view = MovieViews()
        num_of_tickets = get_input('[Please enter number of tickets]: ')
        os.system('clear')
        print('[Current movies]:')
        movie_view.show_all_movies()
        movie_id = get_input('[Choose a movie]: ')
        os.system('clear')
        print('[Projections for the movie]:')
        projection_view = ProjectionView()
        projection_view.show_projections_by_movie_id(movie_id)
        projection_id = get_input('[Choose a projection]: ')
        os.system('clear')

        return (num_of_tickets, movie_id, projection_id)

    def _print_movie_theater(self, occupied_tuples):
        print(BACKGROUND_LINE)
        print('#  [Available seats (marked with a dot)]:')
        print(BACKGROUND_LINE)
        print('   1 2 3 4 5 6 7 8 9 10')
        for row in range(1, 11):
            current_row = ''
            for col in range(1, 11):
                if (row, col) in occupied_tuples:
                    if row == 10 and col == 1:
                        current_row += 'X'
                    else:
                        current_row += ' X'
                else:
                    if row == 10 and col == 1:
                        current_row += '.'
                    else:
                        current_row += ' .'
            print(row, current_row)
        print(BACKGROUND_LINE)

    def _reserve_seats(self, occupied_tuples, num_of_tickets):
        ticket = 0
        seats = []
        while ticket != int(num_of_tickets):
            ticket += 1
            new_reservation = get_input(f'\n[Choose seat [{ticket}] <n, m>]: ')
            row_col = new_reservation.split(', ')
            curr_row = int(row_col[0])
            curr_col = int(row_col[1])

            if (curr_row, curr_col) not in occupied_tuples:
                try:
                    validate_row(curr_row)
                    validate_col(curr_col)
                    seats.append((curr_row, curr_col))
                    occupied_tuples.append((curr_row, curr_col))
                except Exception as exc:
                    ticket -= 1
                    print(str(exc))
                    print('[Try again!]')
                    if (curr_row, curr_col) in occupied_tuples:
                        occupied_tuples.pop()
            else:
                print('[Seat is taken.]')
                print('[Try again!]')
                ticket -= 1

        return seats

    def _confirmation(self, movie_id, projection_id, reserved_seats):
        os.system('clear')
        print(BACKGROUND_LINE)
        print('#  [This is your reservation]:')
        print('#  [Seats]:', reserved_seats)
        confirm = get_input('#  [Confirm - type "finalize"]: ')
        return confirm == 'finalize'


class AdminReservationView(ReservationViews):
    def __init__(self):
        super().__init__()

    def get_all_reservations(self):
        reservations = self.controller.get_all_reservations()
        for reservation in reservations:
            print(BACKGROUND_LINE)
            print(f'[Reservation_ID]: {reservation.id}')
            print(f'[User_ID]:        {reservation.user_id}')
            print(f'[Projection_ID]:  {reservation.projection_id}')
            print(f'[Row]:            {reservation.row}')
            print(f'[Col]:            {reservation.col}')
