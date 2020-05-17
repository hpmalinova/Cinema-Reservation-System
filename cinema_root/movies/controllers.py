from .models import MovieModel


class MovieController:
    def __init__(self):
        self.model = MovieModel

    def add_movie(self, title, movie_year, rating):
        try:
            self.model.add_movie(title, movie_year, rating)
            return f'[Movie with title = {title} was created successfully!]'
        except Exception:
            return f'[Oops, something went wrong.]\n[Try again!]'

    def get_all_movies(self):
        try:
            movies = self.model.get_all_movies()
            return movies
        except Exception:
            return f'[Oops, something went wrong.]\n[Try again!]'

    def get_movie_title(self, movie_id):
        try:
            title = self.model.get_movie_title(movie_id)
            if title:
                return (title, True)
            else:
                return (f'There is no movie with id = {movie_id}.', False)
        except Exception:
            return (f'[Oops, something went wrong.]\n[Try again!]', False)

    def delete_movie(self, movie_id):
        try:
            movie = self.model.get_movie(movie_id)

            if not movie:
                return f'[Movie with id = {movie_id} does not exist.]\n'

            self.model.delete_movie(movie_id=movie_id)
            # Check if movie still exists in the DB
            movie = self.model.get_movie(movie_id=movie_id)

            if not movie:
                return f'[Movie with id = {movie_id} was deleted successfully!]\n'
        except Exception:
            return '[Oops, something went wrong.]\n[Try again!]'
