from cinema_root.db import Database
from .projection_queries import (SELECT_ALL_PROJECTIONS, CREATE_PROJECTION, GET_PROJECTION_ID, DELETE_PROJECTION_BY_ID,
                                 GET_PROJECTION_BY_ID, UPDATE_PROJECTION_TYPE, UPDATE_PROJECTION_DATE,
                                 UPDATE_PROJECTION_TIME, GET_PROJECTION_BY_MOVIE_ID, GET_PROJECTION_BY_PID)


class ProjectionGateway:
    def __init__(self):
        self.db = Database

    def get_all_projections(self):
        self.db.cursor.execute(SELECT_ALL_PROJECTIONS)
        raw_projections = self.db.cursor.fetchall()
        self.db.connection.commit()

        return raw_projections

    def add_projection(self, movie_id, p_type, p_date, p_time):
        # Create Projection in DB
        self.db.cursor.execute(CREATE_PROJECTION, (movie_id, p_type, p_date, p_time))

        # Get Projection ID from DB
        self.db.cursor.execute(GET_PROJECTION_ID, (movie_id, p_type, p_date, p_time))
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
        self.db.cursor.execute(DELETE_PROJECTION_BY_ID, (p_id,))
        self.db.connection.commit()

        print(f'Projection with id: {p_id} was successfully deleted.')

    def get_projection_id(self, p_id):
        self.db.cursor.execute(GET_PROJECTION_BY_ID, (p_id, ))
        projection_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()

        return projection_id

    def update_projection(self, p_id, to_upd, new_value):
        # projection_id = self.get_projection_id(p_id)

        if to_upd == 'type':
            self.db.cursor.execute(UPDATE_PROJECTION_TYPE, (new_value, p_id))
        if to_upd == 'date':
            self.db.cursor.execute(UPDATE_PROJECTION_DATE, (new_value, p_id))
        if to_upd == 'time':
            self.db.cursor.execute(UPDATE_PROJECTION_TIME, (new_value, p_id))

        self.db.connection.commit()

        # if not projection_id:
        #     raise ValueError('You can`t update non existing projection.')

        # print(f'Projection with id: {p_id} was successfully updated.')

    def get_projections_by_movie_id(self, movie_id):
        self.db.cursor.execute(GET_PROJECTION_BY_MOVIE_ID, (movie_id,))
        raw_projections = self.db.cursor.fetchall()
        self.db.connection.commit()

        return raw_projections

    def get_projection_by_id(self, p_id):
        self.db.cursor.execute(GET_PROJECTION_BY_PID, (p_id,))
        projection = self.db.cursor.fetchone()
        self.db.connection.commit()

        return projection
