from cinema_root.db import Database, Projection
from .projection_queries import (SELECT_ALL_PROJECTIONS, CREATE_PROJECTION, GET_PROJECTION_ID, DELETE_PROJECTION_BY_ID,
                                 GET_PROJECTION_BY_ID, UPDATE_PROJECTION_TYPE, UPDATE_PROJECTION_DATE,
                                 UPDATE_PROJECTION_TIME, GET_PROJECTION_BY_MOVIE_ID, GET_PROJECTION_BY_PID)


class ProjectionGateway:
    def __init__(self):
        self.db = Database

    def get_all_projections(self):  # DONE
        session = self.db.create_session()
        raw_projections_dict = []

        try:
            raw_projections = session.query(Projection)
        except Exception:
            session.close()
            return False

        for raw_projection in raw_projections:
            raw_dict = raw_projection.__dict__
            del raw_dict['_sa_instance_state']
            raw_projections_dict.append(raw_dict)

        session.close()
        return raw_projections_dict

    def add_projection(self, movie_id, p_type, p_date, p_time):
        # Create Projection in DB
        self.db.cursor.execute(CREATE_PROJECTION, (movie_id, p_type, p_date, p_time))

        # Get Projection ID from DB
        self.db.cursor.execute(GET_PROJECTION_ID, (movie_id, p_type, p_date, p_time))
        p_id = self.db.cursor.fetchone()[0]
        self.db.connection.commit()

        print(f'Successfully created projection with id={p_id}')

    def delete_projection(self, p_id):  # DONE?
        session = self.db.create_session()

        try:
            session.query(Projection).filter(Projection.p_id == p_id).one()
        except Exception:
            session.close()
            return False

        session.query(Projection).filter(Projection.p_id == p_id).delete()

        session.commit()
        session.close()

        print(f'Projection with id: {p_id} was successfully deleted.')

    def get_projection_id(self, p_id):  # DONE?, ама... WTF??? Защо ни трябва това? :D
        session = self.db.create_session()

        try:
            raw_projection = session.query(Projection).filter(Projection.p_id == p_id).one()
        except Exception:
            session.close()
            return False

        raw_dict = raw_projection.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict["p_id"]

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

    def get_projections_by_movie_id(self, movie_id):  # DONE
        session = self.db.create_session()
        raw_projections_dict = []

        try:
            raw_projections = session.query(Projection).filter(Projection.movie_id == movie_id)
        except Exception:
            session.close()
            return False

        for raw_projection in raw_projections:
            raw_dict = raw_projection.__dict__
            del raw_dict['_sa_instance_state']
            raw_projections_dict.append(raw_dict)

        session.close()
        return raw_projections_dict

    def get_projection_by_id(self, p_id):  # DONE?
        session = self.db.create_session()

        try:
            raw_projection = session.query(Projection).filter(Projection.p_id == p_id).one()
        except Exception:
            session.close()
            return False

        raw_dict = raw_projection.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict
