from cinema_root.db import Database
from .movie_queries import (SELECT_ALL_MOVIES, CREATE_QUERY, GET_MOVIE_ID,
                            GET_MOVIE_BY_ID, DELETE_MOVIE_BY_ID, GET_TITLE_BY_ID)


class MovieGateway:
    def __init__(self):
        self.db = Database()

    def add_movie(self, title, year, rating):
        # Create Movie in DB
        self.db.cursor.execute(CREATE_QUERY, (title, year, rating))

        # Get Movie ID from DB
        self.db.cursor.execute(GET_MOVIE_ID, (title, year))

        movie_id = self.db.cursor.fetchone()[0]

        self.db.connection.commit()
        print(f'Successfully created movie with id={movie_id}')

    def delete_movie(self, id):
        self.db.cursor.execute(DELETE_MOVIE_BY_ID, (id))
        self.db.connection.commit()

    def get_movie(self, id):
        self.db.cursor.execute(GET_MOVIE_BY_ID, (id,))
        movie = self.db.cursor.fetchone()
        self.db.connection.commit()

        return movie

    def get_all_movies(self):
        self.db.cursor.execute(SELECT_ALL_MOVIES)
        raw_movies = self.db.cursor.fetchall()

        self.db.connection.commit()

        return raw_movies

    def get_movie_title(self, id):
        self.db.cursor.execute(GET_TITLE_BY_ID, (id))
        title = self.db.cursor.fetchone()
        self.db.connection.commit()

        return title
