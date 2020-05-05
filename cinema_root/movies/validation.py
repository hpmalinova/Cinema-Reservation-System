YEAR_START = 2019
YEAR_END = 2022
RATING_LOWEST = 0
RATING_HIGHEST = 10


def validate_year(year):
    if year < YEAR_START or year > YEAR_END:
        raise ValueError(f'Year should be between {YEAR_START} and {YEAR_END}')


def validate_rating(rating):
    if rating < 0 or rating > 10:
        raise ValueError(f'Rating should be between {RATING_LOWEST} and {RATING_HIGHEST}')
