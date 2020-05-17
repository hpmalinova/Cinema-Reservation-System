from .controllers import MovieController
from cinema_root.utils import get_input, BACKGROUND_LINE


class MovieViews:
    def __init__(self):
        self.controller = MovieController()

    def show_all_movies(self):
        movies = self.controller.get_all_movies()
        if not movies:
            print('Currently there are no movies.')
        elif isinstance(movies, str):
            print(movies)
        else:
            for movie in movies:
                print(BACKGROUND_LINE)
                print(f'[ID]:     {movie.movie_id}')
                print(f'[Title]:  {movie.title}')
                print(f'[Year]:   {movie.movie_year}')
                print(f'[Rating]: {movie.rating}')

    def get_movie_title(self, movie_id):
        title, success = self.controller.get_movie_title(movie_id)
        if success:
            return title
        else:
            print(title)


class AdminMovieView(MovieViews):
    def __init__(self):
        super().__init__()

    def add_movie(self):
        title = get_input('[Enter title]: ')
        movie_year = get_input('[Enter year]: ')
        rating = get_input('[Enter rating]: ')

        result = self.controller.add_movie(title, movie_year, rating)
        print(result)

    def delete_movie(self):
        movie_id = get_input('[Enter id of the movie you want to delete]: ')

        result = self.controller.delete_movie(movie_id)
        print(result)
