from .validation import validate_type, validate_date_and_time
from .projections_gateway import ProjectionGateway


class ProjectionModel:
    gateway = ProjectionGateway()

    def __init__(self, *, p_id, movie_id, p_type, p_date, p_time):
        self.p_id = p_id
        self.movie_id = movie_id
        self.p_type = p_type
        self.p_date = p_date
        self.p_time = p_time

    @classmethod
    def validate(cls, p_type, p_date, p_time):
        validate_type(p_type)
        validate_date_and_time(p_date, p_time)

    @classmethod
    def get_projection_by_id(cls, p_id):
        projection = cls.gateway.get_projection_by_id(p_id)
        if projection is not None:
            return cls(**projection)

    @classmethod
    def get_all_projections(cls):
        raw_projections = cls.gateway.get_all_projections()

        all_projections = []
        for raw_projection in raw_projections:
            projection_model = cls(**raw_projection)
            all_projections.append(projection_model)

        return all_projections

    @classmethod
    def add_projection(cls, movie_id, p_type, p_date, p_time):
        movie_id = int(movie_id)
        cls.validate(p_type, p_date, p_time)
        cls.gateway.add_projection(movie_id, p_type, p_date, p_time)

    @classmethod
    def delete_projection(cls, p_id):
        cls.gateway.delete_projection(p_id)

    @classmethod
    def update_projection(cls, p_id, to_upd, new_value):
        cls.gateway.update_projection(p_id, to_upd, new_value)

    @classmethod
    def get_projections_by_movie_id(cls, movie_id):
        raw_projections = cls.gateway.get_projections_by_movie_id(movie_id)

        all_projections = []
        for raw_projection in raw_projections:
            projection_model = cls(**raw_projection)
            all_projections.append(projection_model)

        return all_projections
