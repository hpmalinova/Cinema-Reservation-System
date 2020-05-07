from cinema_root.db import Database
from .reservation_queries import (SELECT_ALL_RESERVATIONS, CREATE_QUERY, GET_RESERVATION_BY_PROJ_ID_ROW_COL,
                                  GET_RESERVATION_BY_USER_ID_PROJ_ID_ROW_COL, GET_RESERVATION_BY_ID,
                                  GET_RESERVATIONS_BY_PROJ_ID, DELETE_RESERVATION_BY_ID)


class ReservationGateway:
    def __init__(self):
        self.db = Database()

    def add_reservation(self, user_id, projection_id, row, col):
        self.db.cursor.execute(GET_RESERVATION_BY_PROJ_ID_ROW_COL, (projection_id, row, col))

        occupied = self.db.cursor.fetchone()

        if occupied:
            raise Exception('Seat is taken.')
        else:
            self.db.cursor.execute(CREATE_QUERY, (user_id, projection_id, row, col))
            self.db.cursor.execute(GET_RESERVATION_BY_USER_ID_PROJ_ID_ROW_COL, (user_id, projection_id, row, col))
            raw_reservation = self.db.cursor.fetchone()

            self.db.connection.commit()

            return raw_reservation

    def delete_reservation(self, id):
        # Check if Reservation ID exists in DB
        self.db.cursor.execute(GET_RESERVATION_BY_ID, (id))
        reservation_id = self.db.cursor.fetchone()[0]

        if not reservation_id:
            print('You can`t delete non existing reservation.')
            return

        # Delete Reservation in DB by id
        self.db.cursor.execute(DELETE_RESERVATION_BY_ID, (id))
        self.db.connection.commit()

    def get_occupied_seats(self, projection_id):
        print
        self.db.cursor.execute(GET_RESERVATIONS_BY_PROJ_ID, (projection_id,))
        raw_occupied = self.db.cursor.fetchall()

        self.db.connection.commit()

        return raw_occupied

    def get_all_reservations(self):
        self.db.cursor.execute(SELECT_ALL_RESERVATIONS)
        raw_reservations = self.db.cursor.fetchall()

        self.db.connection.commit()

        return raw_reservations
