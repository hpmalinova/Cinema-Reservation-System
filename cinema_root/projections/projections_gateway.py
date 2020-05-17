from cinema_root.db_schema import Projection
from cinema_root.db import session_scope


class ProjectionGateway:
    def get_all_projections(self):
        with session_scope() as session:
            raw_projections_dict = []
            raw_projections = session.query(Projection)

            for raw_projection in raw_projections:
                raw_dict = raw_projection.__dict__
                del raw_dict['_sa_instance_state']
                raw_projections_dict.append(raw_dict)

            return raw_projections_dict

    def add_projection(self, movie_id, p_type, p_date, p_time):
        with session_scope() as session:
            projection = Projection(movie_id=movie_id, p_type=p_type, p_date=p_date, p_time=p_time)
            session.add(projection)

            raw_projection = session.query(Projection).filter(Projection.movie_id == movie_id)\
                                                      .filter(Projection.p_type == p_type)\
                                                      .filter(Projection.p_date == p_date)\
                                                      .filter(Projection.p_time == p_time)\
                                                      .one()

            raw_dict = raw_projection.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict

    def delete_projection(self, p_id):  # DONE?
        with session_scope() as session:
            session.query(Projection).filter(Projection.p_id == p_id).delete()

    # TODO FIX? ZASHTO NI E
    def get_projection_id(self, p_id):  # DONE?, ама... WTF??? Защо ни трябва това? :D
        with session_scope() as session:
            raw_projection = session.query(Projection).filter(Projection.p_id == p_id).one()

            raw_dict = raw_projection.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict["p_id"]

    def update_projection(self, p_id, to_upd, new_value):
        with session_scope() as session:
            session.query(Projection).filter(Projection.p_id == p_id).update({f'{to_upd}': f'{new_value}'})

    def get_projections_by_movie_id(self, movie_id):
        with session_scope() as session:
            raw_projections_dict = []
            raw_projections = session.query(Projection).filter(Projection.movie_id == movie_id)

            for raw_projection in raw_projections:
                raw_dict = raw_projection.__dict__
                del raw_dict['_sa_instance_state']
                raw_projections_dict.append(raw_dict)

            return raw_projections_dict

    def get_projection_by_id(self, p_id):
        with session_scope() as session:
            raw_projection = session.query(Projection).filter(Projection.p_id == p_id).one()

            raw_dict = raw_projection.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict
