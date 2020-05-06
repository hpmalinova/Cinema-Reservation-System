from .projections_gateway import ProjectionGateway


class MovieController:
    def __init__(self):
        self.gateway = ProjectionGateway()

    def add_projection(self, movie_id, p_type, p_date, p_time):
        return self.gateway.add_projection(self, movie_id, p_type, p_date, p_time)

    def delete_projection(self, p_id):
        return self.gateway.delete_projection(p_id)

    # delete_old_projections

    def show_all_projections(self):
        return self.gateway.show_all_projections()

    def update_projection_type(self, p_id, new_p_type):
        return self.gateway.update_projection_type(p_id, new_p_type)

    def update_projection(self, p_id, to_upd, new_value):
        return self.gateway.update_projection_type(p_id, to_upd, new_value)

    # def update_projection_date(self, p_id, new_p_date):
    #     return self.gateway.update_projection_date(p_id, new_p_date)

    # def update_projection_time(self, p_id, new_p_time):
    #     return self.gateway.uptime_projection_time(p_id, new_p_time)
