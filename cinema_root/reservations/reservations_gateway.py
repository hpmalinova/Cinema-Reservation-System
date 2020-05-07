from cinema_root.db import Database
from .models import ReservationModel
from .reservation_queries import SELECT_ALL_RESERVATIONS


class ReservationGateway:
    def __init__(self):
        self.model = ReservationModel
        self.db = Database()

    def add_reservation(self, user_id, projection_id, row, col):
        self.model.validate(row, col)
        get_query = '''
            SELECT *
                FROM reservations
                WHERE projection_id=? AND row=? AND col=?
        '''
        self.db.cursor.execute(get_query, (projection_id, row, col))

        occupied = self.db.cursor.fetchone()

        if occupied:
            raise Exception('Seat is taken.')
        else:
            add_reservation_query = '''
                INSERT INTO reservations(user_id, projection_id, row, col)
                VALUES(?, ?, ?, ?);
            '''
            # fix?
            # self.db.cursor = self.db.connection.cursor()
            self.db.cursor.execute(add_reservation_query, (user_id, projection_id, row, col))

            get_new_reservation_query = '''
                SELECT *
                    FROM reservations
                    WHERE user_id=? AND projection_id=? AND row=? AND col=?
            '''
            self.db.cursor.execute(get_new_reservation_query, (user_id, projection_id, row, col))
            reservation = self.db.cursor.fetchone()

            self.db.connection.commit()
            return self.model(
                reservation_id=reservation[0],
                user_id=reservation[1],
                projection_id=reservation[2],
                row=reservation[3],
                col=reservation[4])

    def delete_reservation(self, id):
        select_user_query = 'SELECT * FROM reservations WHERE id=?;'
        self.db.cursor.execute(select_user_query, (id))
        raw_user = self.db.cursor.fetchone()

        if raw_user:
            delete_user_query = 'DELETE FROM reservations WHERE id=?;'
            self.db.cursor.execute(delete_user_query, (id))
            self.db.connection.commit()
        else:
            raise Exception('Reservation not found.')

    def get_occupied_seats(self, projection_id):
        select_user_query = 'SELECT * FROM reservations WHERE projection_id=?;'
        self.db.cursor.execute(select_user_query, (projection_id))
        raw_occupied = self.db.cursor.fetchall()

        all_occupied = []
        for seat in raw_occupied:
            all_occupied.append(
                self.model(reservation_id=seat[0], user_id=seat[1], projection_id=seat[2], row=seat[3], col=seat[4])
            )

        return all_occupied

    def get_all_reservations(self):
        self.db.cursor.execute(SELECT_ALL_RESERVATIONS)
        raw_reservations = self.db.cursor.fetchall()

        self.db.connection.commit()

        all_reservations = []
        for reservation in raw_reservations:
            all_reservations.append(self.model(user_id=reservation[0], projection_id=reservation[1],
                                               row=reservation[2], col=reservation[3]))

        return all_reservations
