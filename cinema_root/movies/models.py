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

    '''
    @classmethod
    def get_all_movies(cls):
        raw_movies = gateway.get_all_movies()
        for raw_movie in raw_movies:  # To model
                movie_model = cls(**raw_movie)
                all_movies.append(movie_model)

        return all_movies
    '''
