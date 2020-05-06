from .models import ProjectionModel


class ProjectionController:
    def __init__(self):
        self.model = ProjectionModel

    def get_all_projections(self):
        return self.model.get_all_projections()

    # NO RETURN?????
    def add_projection(self, movie_id, p_type, p_date, p_time):
        self.model.add_projection(movie_id, p_type, p_date, p_time)

    def delete_projection(self, p_id):
        self.model.delete_projection(p_id)

    def update_projection(self, p_id, to_upd, new_value):
        return self.model.update_projection(p_id, to_upd, new_value)

    def get_projections_by_movie_id(self, movie_id):
        return self.model.get_projections_by_movie_id(movie_id)

    # TODO
    # delete_old_projections
