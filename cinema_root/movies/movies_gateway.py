from cinema_root.db import Database, Movie


class MovieGateway:
    def __init__(self):
        self.db = Database

    def add_movie(self, title, year, rating):  # DONE?
        session = self.db.create_session()

        session.add_all([
            Movie(title=title, year=year, rating=rating)
        ])
        session.commit()

        raw_movie = session.query(Movie).filter(Movie.title == title)\
                                        .filter(Movie.year == year)\
                                        .filter(Movie.rating == rating)\
                                        .one()

        raw_dict = raw_movie.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict

    def delete_movie(self, id):  # DONE?
        session = self.db.create_session()

        try:
            session.query(Movie).filter(Movie.id == id).one()
        except Exception:
            session.close()
            return False

        session.query(Movie).filter(Movie.id == id).delete()

        session.commit()
        session.close()

    def get_movie(self, id):  # DONE?
        session = self.db.create_session()

        try:
            raw_movie = session.query(Movie).filter(Movie.id == id).one()
        except Exception:
            session.close()
            return False

        raw_dict = raw_movie.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict

    def get_all_movies(self):  # DONE?
        session = self.db.create_session()
        raw_movies_dict = []

        try:
            raw_movies = session.query(Movie)
        except Exception:
            session.close()
            return False

        for raw_movie in raw_movies:
            raw_dict = raw_movie.__dict__
            del raw_dict['_sa_instance_state']
            raw_movies_dict.append(raw_dict)

        session.close()
        return raw_movies_dict

    def get_movie_title(self, id):  # DONE?
        session = self.db.create_session()

        try:
            raw_movie = session.query(Movie).filter(Movie.id == id).one()
        except Exception:
            session.close()
            return False

        raw_dict = raw_movie.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict["title"]
