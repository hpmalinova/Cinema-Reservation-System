from .validation import validate_year, validate_rating


class MovieModel:
    def __init__(self, *, movie_id, title, year, rating):
        self.movie_id = movie_id
        self.title = title
        self.year = year
        self.rating = rating

    @staticmethod
    def validate(year, rating):
        validate_year(year)
        validate_rating(rating)
