from .validation import validate_row, validate_col
from .reservations_gateway import ReservationGateway


class ReservationModel:
    gateway = ReservationGateway()

    def __init__(self, *, reservation_id, user_id, projection_id, row, col):
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.projection_id = projection_id
        self.row = row
        self.col = col

    @classmethod
    def validate(cls, row, col):
        validate_row(row)
        validate_col(col)

    @classmethod
    def add_reservation(cls, user_id, projection_id, row, col):
        user_id = int(user_id)
        projection_id = int(projection_id)
        row = int(row)
        col = int(col)
        cls.validate(row, col)
        cls.gateway.add_reservation(user_id, projection_id, row, col)

    @classmethod
    def get_occupied_seats(cls, projection_id):
        raw_occupied = cls.gateway.get_occupied_seats()

        all_occupied = []
        for raw in raw_occupied:
            reservation_model = cls(**raw)
            all_occupied.append(reservation_model)

        return all_occupied

    @classmethod
    def get_all_reservations(cls):
        raw_reservations = cls.gateway.get_all_reservations()

        all_reservations = []
        for raw_reservation in raw_reservations:
            reservation_model = cls(**raw_reservation)
            all_reservations.append(reservation_model)

        return all_reservations
