from cinema_root.db_schema import Movie
from cinema_root.db import session_scope


class MovieGateway:
    def add_movie(self, title, movie_year, rating):
        with session_scope() as session:
            movie = Movie(title=title, movie_year=movie_year, rating=rating)
            session.add(movie)

    def delete_movie(self, movie_id):
        with session_scope() as session:
            session.query(Movie).filter(Movie.movie_id == movie_id).delete()

    def get_movie(self, movie_id):
        with session_scope() as session:
            raw_movie = session.query(Movie).filter(Movie.movie_id == movie_id).one()

            raw_dict = raw_movie.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict

    def get_all_movies(self):
        with session_scope() as session:
            raw_movies_dict = []
            raw_movies = session.query(Movie)

            for raw_movie in raw_movies:
                raw_dict = raw_movie.__dict__
                del raw_dict['_sa_instance_state']
                raw_movies_dict.append(raw_dict)

            return raw_movies_dict

    def get_movie_title(self, movie_id):
        with session_scope() as session:
            raw_movie = session.query(Movie).filter(Movie.movie_id == movie_id).one()

            raw_dict = raw_movie.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict["title"]
