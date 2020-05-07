from .models import MovieModel


class MovieController:
    def __init__(self):
        self.model = MovieModel

    def add_movie(self, title, year, rating):
        self.model.add_movie(title, year, rating)

    def delete_movie(self, id):
        self.model.delete_movie(id)

    def get_all_movies(self):
        return self.model.get_all_movies()

    def get_movie_title(self, id):
        return self.model.get_movie_title(id)
