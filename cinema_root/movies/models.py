from .validation import validate_year, validate_rating
from .movies_gateway import MovieGateway


class MovieModel:
    gateway = MovieGateway()

    def __init__(self, *, movie_id, title, movie_year, rating):
        self.movie_id = movie_id
        self.title = title
        self.movie_year = movie_year
        self.rating = rating

    @classmethod
    def validate(cls, movie_year, rating):
        validate_year(movie_year)
        validate_rating(rating)

    @classmethod
    def add_movie(cls, title, movie_year, rating):
        movie_year = int(movie_year)
        rating = float(rating)
        cls.validate(movie_year, rating)
        cls.gateway.add_movie(title, movie_year, rating)

    @classmethod
    def get_movie(cls, movie_id):
        movie = cls.gateway.get_movie(movie_id)
        if movie:
            return cls(**movie)

    @classmethod
    def get_all_movies(cls):
        raw_movies = cls.gateway.get_all_movies()

        all_movies = []
        for raw_movie in raw_movies:
            movie_model = cls(**raw_movie)
            all_movies.append(movie_model)

        return all_movies

    @classmethod
    def get_movie_title(cls, movie_id):
        return cls.gateway.get_movie_title(movie_id)

    @classmethod
    def delete_movie(cls, movie_id):
        cls.gateway.delete_movie(movie_id)
