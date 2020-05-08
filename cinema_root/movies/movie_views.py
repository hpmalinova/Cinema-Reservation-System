from .controllers import MovieController
from cinema_root.utils import get_input
from ..utils import BACKGROUND_LINE


class MovieViews:
    def __init__(self):
        self.controller = MovieController()

    def show_all_movies(self):
        movies = self.controller.get_all_movies()
        for movie in movies:
            print(BACKGROUND_LINE)
            print(f'[ID]:     {movie.id}')
            print(f'[Title]:  {movie.title}')
            print(f'[Year]:   {movie.year}')
            print(f'[Rating]: {movie.rating}')

    def get_movie_title(self, id):
        return self.controller.get_movie_title(id)


class AdminMovieView(MovieViews):
    def __init__(self):
        super().__init__()

    def add_movie(self):
        title = get_input('[Enter title]: ')
        year = get_input('[Enter year]: ')
        rating = get_input('[Enter rating]: ')

        self.controller.add_movie(title, year, rating)

    def delete_movie(self):
        movie_id = get_input('[Enter id of the movie you want to delete]: ')
        #if self.controller.delete_movie(movie_id):
        #    print(f'Movie with id = {movie_id} has been deleted successfully!')
        #else:
        #    print(f'Something happened! The movie with id = {movie_id} could not be deleted.')
