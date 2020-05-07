from .models import ReservationModel


class ReservationController:
    def __init__(self):
        self.model = ReservationModel

    def add_reservation(self, user_id, projection_id, row, col):
        reservation = self.model.add_reservation(user_id, projection_id, row, col)
        with open('log.txt', 'a+') as f:
            f.write(f'ID: {reservation.id} ')
            f.write(f'ProjectionID: {reservation.projection_id} ')
            f.write(f'UserID: {reservation.user_id} ')
            f.write(f'Row: {reservation.row} ')
            f.write(f'Column: {reservation.col}\n')

    def delete_reservation(self, id):
        self.model.delete_reservation(id)

    def get_occupied_seats(self, projection_id):
        return self.model.get_occupied_seats(projection_id)

    def get_all_reservations(self):
        return self.model.get_all_reservations()
