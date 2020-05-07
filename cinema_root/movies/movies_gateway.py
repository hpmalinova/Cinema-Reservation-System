from cinema_root.db import Database
from .models import MovieModel
from .movie_queries import SELECT_ALL_MOVIES


class MovieGateway:
    def __init__(self):
        self.model = MovieModel
        self.db = Database()

    def add_movie(self, title, year, rating):
        year = int(year)
        rating = float(rating)
        self.model.validate(year, rating)

        # Create Movie in DB
        create_query = '''
            INSERT INTO movies (title, year, rating)
            VALUES (?, ?, ?);
        '''
        self.db.cursor.execute(create_query, (title, year, rating))

        # Get Movie ID from DB
        get_id_query = f'''
        SELECT id
            FROM movies
            WHERE title= \'{title}\' and year=\'{year}\';'''
        self.db.cursor.execute(get_id_query)

        movie_id = self.db.cursor.fetchone()[0]

        self.db.connection.commit()
        print(f'Successfully created movie with id={movie_id}')
        return self.model(movie_id=movie_id, title=title,
                          year=year, rating=rating)

    def delete_movie(self, id):
        # Check if Movie ID exists in DB
        get_id_query = f'''
        SELECT *
            FROM movies
            WHERE id= \'{id}\';
        '''
        self.db.cursor.execute(get_id_query)
        movie_id = self.db.cursor.fetchone()[0]

        if not movie_id:
            print('You can`t delete non existing movie.')
            return

        # Delete Movie in DB by id
        delete_query = f'''
            DELETE FROM movies
                WHERE id= \'{id}\'
        '''
        self.db.cursor.execute(delete_query)

        self.db.connection.commit()

        print(f'Movie with id: {id} was successfully deleted.')

    def show_all_movies(self):
        self.db.cursor.execute(SELECT_ALL_MOVIES)
        raw_movies = self.db.cursor.fetchall()

        self.db.connection.commit()

        all_movies = []

        for raw_movie in raw_movies:  # To model
            movie_model = self.model(movie_id=raw_movie[0], title=raw_movie[1],
                                     year=raw_movie[2], rating=raw_movie[3])
            all_movies.append(movie_model)

        return all_movies
