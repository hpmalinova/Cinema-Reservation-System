from .models import MovieModel


class MovieController:
    def __init__(self):
        self.model = MovieModel

    def add_movie(self, title, movie_year, rating):
        self.model.add_movie(title, movie_year, rating)

    def delete_movie(self, movie_id):
        self.model.delete_movie(movie_id)
        # Check if Movie still exists in DB
        movie = self.model.get_movie(movie_id)
        return True if movie is None else False

    def get_all_movies(self):
        return self.model.get_all_movies()

    def get_movie_title(self, movie_id):
        return self.model.get_movie_title(movie_id)
