from cinema_root.db import Database, Projection


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

    def add_projection(self, movie_id, p_type, p_date, p_time):  # DONE?
        session = self.db.create_session()

        session.add_all([
            Projection(movie_id=movie_id, p_type=p_type, p_date=p_date, p_time=p_time)
        ])
        session.commit()

        raw_projection = session.query(Projection).filter(Projection.movie_id == movie_id)\
                                                  .filter(Projection.p_type == p_type)\
                                                  .filter(Projection.p_date == p_date)\
                                                  .filter(Projection.p_time == p_time)\
                                                  .one()

        raw_dict = raw_projection.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict

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

    def update_projection(self, p_id, to_upd, new_value):  # DONE?
        session = self.db.create_session()

        try:
            session.query(Projection).filter(Projection.p_id == p_id).update({f'{to_upd}': f'{new_value}'})
        except Exception:
            session.close()
            return False

        session.commit()
        session.close()

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
