from .validation import validate_year, validate_rating
from .movies_gateway import MovieGateway


class MovieModel:
    gateway = MovieGateway()

    def __init__(self, *, id, title, year, rating):
        self.id = id
        self.title = title
        self.year = year
        self.rating = rating

    @classmethod
    def validate(cls, year, rating):
        validate_year(year)
        validate_rating(rating)

    @classmethod
    def get_all_movies(cls):
        raw_movies = cls.gateway.get_all_movies()

        all_movies = []
        for raw_movie in raw_movies:
            movie_model = cls(**raw_movie)
            all_movies.append(movie_model)

        return all_movies

    @classmethod
    def get_movie_title(cls, id):
        return cls.gateway.get_movie_title(id)

    @classmethod
    def add_movie(cls, title, year, rating):
        year = int(year)
        rating = float(rating)
        cls.validate(year, rating)
        cls.gateway.add_movie(title, year, rating)

    @classmethod
    def delete_movie(cls, id):
        cls.gateway.delete_movie(id)
