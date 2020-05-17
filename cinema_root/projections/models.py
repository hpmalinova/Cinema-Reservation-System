from .validation import validate_type, validate_date_and_time
from .projections_gateway import ProjectionGateway


class ProjectionModel:
    gateway = ProjectionGateway()

    def __init__(self, *, projection_id, movie_id, projection_type, projection_date, projection_time):
        self.projection_id = projection_id
        self.movie_id = movie_id
        self.projection_type = projection_type
        self.projection_date = projection_date
        self.projection_time = projection_time

    @classmethod
    def validate(cls, projection_type, projection_date, projection_time):
        validate_type(projection_type)
        validate_date_and_time(projection_date, projection_time)

    @classmethod
    def get_projection_by_id(cls, projection_id):
        projection = cls.gateway.get_projection_by_id(projection_id)
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
    def add_projection(cls, movie_id, projection_type, projection_date, projection_time):
        movie_id = int(movie_id)
        cls.validate(projection_type, projection_date, projection_time)
        cls.gateway.add_projection(movie_id, projection_type, projection_date, projection_time)

    @classmethod
    def delete_projection(cls, projection_id):
        cls.gateway.delete_projection(projection_id)

    @classmethod
    def update_projection(cls, projection_id, to_upd, new_value):
        cls.gateway.update_projection(projection_id, to_upd, new_value)

    @classmethod
    def get_projections_by_movie_id(cls, movie_id):
        raw_projections = cls.gateway.get_projections_by_movie_id(movie_id)

        all_projections = []
        for raw_projection in raw_projections:
            projection_model = cls(**raw_projection)
            all_projections.append(projection_model)

        return all_projections
