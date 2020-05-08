from .controllers import ProjectionController
from .validation import ALL_UPDATES
from cinema_root.utils import get_input
from ..utils import BACKGROUND_LINE


class ProjectionView:
    def __init__(self):
        self.controller = ProjectionController()

    def show_all_projections(self):
        projections = self.controller.get_all_projections()
        for projection in projections:
            print(BACKGROUND_LINE)
            print(f'ID:       {projection.p_id}')
            print(f'Movie_ID: {projection.movie_id}')
            print(f'Type:     {projection.p_type}')
            print(f'Date:     {projection.p_date}')
            print(f'Time:     {projection.p_time}')

    def show_projections_by_movie_id(self, movie_id):
        projections = self.controller.get_projections_by_movie_id(movie_id)

        if not projections:
            print(f'[No projections for movie with id = [{movie_id}]]')
            return
        for projection in projections:
            print(BACKGROUND_LINE)
            print(f'ID:       {projection.p_id}')
            print(f'Movie_ID: {projection.movie_id}')
            print(f'Type:     {projection.p_type}')
            print(f'Date:     {projection.p_date}')
            print(f'Time:     {projection.p_time}')


class AdminProjectionView(ProjectionView):
    def __init__(self):
        super().__init__()

    def add_projection(self):
        print(BACKGROUND_LINE)
        movie_id = get_input('[Enter movie_id]: ')
        p_type = get_input('[Enter projection type]: ')
        p_date = get_input('[Enter projection date /YYYY-MM-DD/]: ')
        p_time = get_input('[Enter projection time /HH-MM/]: ')

        self.controller.add_projection(movie_id, p_type, p_date, p_time)

    def delete_projection(self):
        print(BACKGROUND_LINE)
        projection_id = get_input('[Enter id of the projection you want to delete]: ')
        self.controller.delete_projection(projection_id)

    def update_projection(self):
        print(BACKGROUND_LINE)
        projection_id = get_input('[Enter projection id]: ')
        what_to_update = self._get_to_update('[Enter what you want to update /type, date, time/]:')
        new_value = get_input('[Enter new value]: ')
        if self.controller.update_projection(projection_id, what_to_update, new_value):
            print(f'Projection with id={projection_id} was successfully updated.')
        else:
            print(f'Oops, something went wrong.\nProjection with id={projection_id} was not updated.')

    def _get_to_update(self, msg):
        what_to_update = input(msg)

        while what_to_update not in ALL_UPDATES:
            what_to_update = input(msg)

        return what_to_update
