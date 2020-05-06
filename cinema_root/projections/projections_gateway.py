from cinema_root.db import Database
from .models import ProjectionModel
from .projection_queries import SELECT_ALL_PROJECTIONS


class ProjectionGateway:
    def __init__(self):
        self.model = ProjectionModel
        self.db = Database()

    def add_projection(self, movie_id, p_type, p_date, p_time):
        movie_id = int(movie_id)
        self.model.validate(p_type, p_date, p_time)

        # Create Projection in DB
        create_query = '''
            INSERT INTO projections (movie_id, p_type, p_date, p_time)
            VALUES (?, ?, ?, ?);
        '''
        self.db.cursor.execute(create_query, (movie_id, p_type, p_date, p_time))

        # Get Movie ID from DB
        get_id_query = f'''
        SELECT p_id
            FROM movies
            WHERE p_date= \'{p_date}\' and p_type=\'{p_type}\';'''
        self.db.cursor.execute(get_id_query)

        p_id = self.db.cursor.fetchone()[0]

        self.db.connection.commit()
        print(f'Successfully created projection with id={p_id}')
        return self.model(p_id=p_id, movie_id=movie_id, p_type=p_type,
                          p_date=p_date, p_time=p_time)

    def delete_projection(self, p_id):
        # Check if Projection ID exists in DB
        projection_id = self.get_projection_id(p_id)
        # get_id_query = f'''
        # SELECT *
        #     FROM projections
        #     WHERE p_id= \'{id}\';
        # '''
        # self.db.cursor.execute(get_id_query)
        # projection_id = self.db.cursor.fetchone()[0]

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

    def show_all_projections(self):
        self.db.cursor.execute(SELECT_ALL_PROJECTIONS)
        raw_projections = self.db.cursor.fetchall()

        self.db.connection.commit()

        all_projections = []

        for raw_projection in raw_projections:
            projection_model = self.model(p_id=raw_projection[0], movie_id=int(raw_projection[1]),
                                          p_type=raw_projection[2], p_date=raw_projection[3],
                                          p_time=raw_projection[4])
            all_projections.append(projection_model)

        return all_projections

    def get_projection_id(self, p_id):
        get_id_query = f'''
        SELECT p_id
            FROM projections
            WHERE p_id= \'{p_id}\';
        '''
        self.db.cursor.execute(get_id_query)
        raw_projection_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()

        return raw_projection_id

    def update_projection_type(self, p_id, new_p_type):
        projection_id = self.get_projection_id(p_id)

        if not projection_id:
            raise ValueError('You can`t update non existing projection.')

        update_query = f'''
            UPDATE projections
                SET p_type = \'{new_p_type}\'
                WHERE p_id= \'{p_id}\'
        '''
        self.db.cursor.execute(update_query)

        self.db.connection.commit()

        print(f'Projection with id: {p_id} was successfully updated.')

    def update_projection(self, p_id, to_upd, new_value):
        available_updates = ['p_type', 'p_date', 'p_time']

        if to_upd not in available_updates:
            raise ValueError(f'You can`t update {to_upd}')

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
