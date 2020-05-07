from .reservations_gateway import ReservationGateway


class ReservationController:
    def __init__(self):
        self.gateway = ReservationGateway()

    def add_reservation(self, user_id, projection_id, row, col):
        return self.gateway.add_reservation(user_id, projection_id, row, col)

    def delete_reservation(self, id):
        return self.gateway.delete_reservation(id)

    def get_occupied_seats(self, projection_id):
        return self.gateway.get_occupied_seats(projection_id)

    def get_all_reservations(self):
        return self.gateway.get_all_reservations()
