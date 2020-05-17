from .models import ProjectionModel


class ProjectionController:
    def __init__(self):
        self.model = ProjectionModel

    def get_all_projections(self):
        return self.model.get_all_projections()

    def add_projection(self, movie_id, projection_type, projection_date, projection_time):
        self.model.add_projection(movie_id, projection_type, projection_date, projection_time)

    def delete_projection(self, projection_id):
        self.model.delete_projection(projection_id)

    def update_projection(self, projection_id, to_upd, new_value):
        projection = self.model.get_projection_by_id(projection_id)

        if projection is not None:
            self.model.update_projection(projection_id, to_upd, new_value)
            return True

        return False

    def get_projections_by_movie_id(self, movie_id):
        return self.model.get_projections_by_movie_id(movie_id)
