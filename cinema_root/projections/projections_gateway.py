from cinema_root.db import Database
from .projection_queries import SELECT_ALL_PROJECTIONS


class ProjectionGateway:
    def __init__(self):
        self.db = Database()

    def get_all_projections(self):
        self.db.cursor.execute(SELECT_ALL_PROJECTIONS)
        raw_projections = self.db.cursor.fetchall()

        self.db.connection.commit()

        return raw_projections

    def add_projection(self, movie_id, p_type, p_date, p_time):
        # Create Projection in DB
        create_query = '''
            INSERT INTO projections (movie_id, p_type, p_date, p_time)
            VALUES (?, ?, ?, ?);
        '''
        self.db.cursor.execute(create_query, (movie_id, p_type, p_date, p_time))

        # Get Projection ID from DB
        get_id_query = f'''
        SELECT p_id
            FROM projections
            WHERE movie_id= \'{movie_id}\' and p_type=\'{p_type}\'
                and p_date= \'{p_date}\' and p_time=\'{p_time}\';
        '''
        self.db.cursor.execute(get_id_query)

        p_id = self.db.cursor.fetchone()[0]

        self.db.connection.commit()

        print(f'Successfully created projection with id={p_id}')

    def delete_projection(self, p_id):
        # Check if Projection ID exists in DB
        projection_id = self.get_projection_id(p_id)

        if not projection_id:
            print('You can`t delete non existing projection.')
            return

        # Delete Projection in DB by id
        delete_query = f'''
            DELETE FROM projections
                WHERE p_id= \'{p_id}\'
        '''
        self.db.cursor.execute(delete_query)
        self.db.connection.commit()

        print(f'Projection with id: {p_id} was successfully deleted.')

    def get_projection_id(self, p_id):
        get_id_query = f'''
        SELECT p_id
            FROM projections
            WHERE p_id= \'{p_id}\';
        '''
        self.db.cursor.execute(get_id_query)
        projection_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()

        return projection_id

    def update_projection(self, p_id, to_upd, new_value):
        projection_id = self.get_projection_id(p_id)

        if not projection_id:
            raise ValueError('You can`t update non existing projection.')

        update_query = f'''
            UPDATE projections
                SET {to_upd} = \'{new_value}\'
                WHERE p_id= \'{p_id}\'
        '''
        self.db.cursor.execute(update_query)
        self.db.connection.commit()

        print(f'Projection with id: {p_id} was successfully updated.')

    def get_projections_by_movie_id(self, movie_id):
        select_query = f'''
        SELECT *
            FROM projections
            WHERE movie_id= \'{movie_id}\';
        '''
        self.db.cursor.execute(select_query)
        raw_projections = self.db.cursor.fetchall()
        self.db.connection.commit()

        return raw_projections
