from .validation import validate_row, validate_col


class ReservationModel:
    def __init__(self, *, reservation_id, user_id, projection_id, row, col):
        self.reservation_id = reservation_id
        self.user_id = user_id
        self.projection_id = projection_id
        self.row = row
        self.col = col

    @staticmethod
    def validate(row, col):
        validate_row(row)
        validate_col(col)
