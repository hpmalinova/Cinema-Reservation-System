from .controllers import ProjectionController
from .validation import ALL_UPDATES


class ProjectionView:
    def __init__(self):
        self.controller = ProjectionController()

    def show_all_projections(self):
        projections = self.controller.get_all_projections()
        for projection in projections:
            print(f'''
    ------------------
    ID: {projection.p_id}
    Movie_ID: {projection.movie_id}
    Type: {projection.p_type}
    Date: {projection.p_date}
    Time: {projection.p_time}
    ------------------''')

    def show_projections_by_movie_id(self):
        movie_id = self.get_input('Enter id: ')
        projections = self.controller.get_projections_by_movie_id(movie_id)

        if not projections:
            print(f'No projections for movie with id={movie_id}')
            return
        for projection in projections:
            print(f'''
    ------------------
    ID: {projection.p_id}
    Movie_ID: {projection.movie_id}
    Type: {projection.p_type}
    Date: {projection.p_date}
    Time: {projection.p_time}
    ------------------''')

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var


class AdminProjectionView(ProjectionView):
    def __init__(self):
        super().__init__()

    def add_projection(self):
        movie_id = self.get_input('Enter movie_id: ')
        p_type = self.get_input('Enter projection type: ')
        p_date = self.get_input('Enter projection date /YYYY-MM-DD/ : ')
        p_time = self.get_input('Enter projection time /HH-MM/ : ')

        self.controller.add_projection(movie_id, p_type, p_date, p_time)

    def delete_projection(self):
        projection_id = self.get_input('Enter id of the projection you want to delete: ')
        self.controller.delete_projection(projection_id)

    def update_projection(self):
        projection_id = self.get_input('Enter projection id: ')
        what_to_update = self.get_to_update('Enter what you want to update /p_type, p_date, p_time/ :')
        new_value = self.get_input('Enter new value: ')
        self.controller.update_projection(projection_id, what_to_update, new_value)

    # MOVE TO UTILS
    def get_to_update(self, msg):
        what_to_update = input(msg)

        while what_to_update not in ALL_UPDATES:
            what_to_update = input(msg)

        return what_to_update
