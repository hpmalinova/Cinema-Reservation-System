from cinema_root.db import Database
from .movie_queries import SELECT_ALL_MOVIES


class MovieGateway:
    def __init__(self):
        self.db = Database()

    def add_movie(self, title, year, rating):
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

    def get_all_movies(self):
        self.db.cursor.execute(SELECT_ALL_MOVIES)
        raw_movies = self.db.cursor.fetchall()

        self.db.connection.commit()

        return raw_movies

    def get_movie_title(self, id):
        select_query = f'''
            SELECT title
                FROM movies
            WHERE id= \'{id}\'
        '''

        self.db.cursor.execute(select_query)
        title = self.db.cursor.fetchone()
        self.db.connection.commit()

        return title
