from .validation import validate_type, validate_date_and_time


class ProjectionModel:
    def __init__(self, *, p_id, movie_id, p_type, p_date, p_time):
        self.p_id = p_id
        self.movie_id = movie_id
        self.p_type = p_type
        self.p_date = p_date
        self.p_time = p_time

    @staticmethod
    def validate(p_type, p_date, p_time):
        validate_type(p_type)
        validate_date_and_time(p_date, p_time)
