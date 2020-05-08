from .models import ReservationModel


class ReservationController:
    def __init__(self):
        self.model = ReservationModel

    def log_info(self, *args1):
        def helper(*kwargs):
            reservation = kwargs[0].model.add_reservation(kwargs[1], kwargs[2], kwargs[3], kwargs[4])
            with open('log.txt', 'a+') as f:
                f.write(f'ID: {reservation.id} ')
                f.write(f'ProjectionID: {reservation.projection_id} ')
                f.write(f'UserID: {reservation.user_id} ')
                f.write(f'Row: {reservation.row} ')
                f.write(f'Column: {reservation.col}\n')
        return helper

    @log_info
    def add_reservation(self, user_id, projection_id, row, col):
        self.model.add_reservation(user_id, projection_id, row, col)

    def delete_reservation(self, user_id, reservation_id):
        self.model.delete_reservation(user_id, reservation_id)
        # Check if Reservation ID still exists in DB
        reservation = self.model.find_reservation(reservation_id)
        return True if reservation is None else False

    def get_occupied_seats(self, projection_id):
        return self.model.get_occupied_seats(projection_id)

    def get_all_reservations(self):
        return self.model.get_all_reservations()

    def get_my_reservations(self, user_id):
        return self.model.get_my_reservations(user_id)
