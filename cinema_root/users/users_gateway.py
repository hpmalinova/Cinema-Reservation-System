from cinema_root.db import Database, User


class UserGateway:
    def __init__(self):
        self.db = Database

    def add_user(self, *, email, hashed_password):  # DONE
        session = self.db.create_session()

        session.add_all([
            User(email=email, password=hashed_password, user_type="Client")
        ])
        session.commit()

        raw_user = session.query(User).filter(User.email == email).one()

        raw_dict = raw_user.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict

    def login(self, *, email, hashed_password):  # DONE
        session = self.db.create_session()

        try:
            raw_user = session.query(User).filter(User.email == email).one()
        except Exception:
            session.close()
            return False

        if hashed_password == raw_user.__dict__['password']:
            raw_dict = raw_user.__dict__
            del raw_dict['_sa_instance_state']
            session.close()
            return raw_dict
        else:
            session.close()
            return False

    def get_user(self, *, id):  # DONE
        session = self.db.create_session()

        try:
            raw_user = session.query(User).filter(User.id == id).one()
        except Exception:
            session.close()
            return False

        raw_dict = raw_user.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict

    def get_all_users(self):  # DONE
        session = self.db.create_session()
        raw_users_dict = []

        try:
            raw_users = session.query(User)
        except Exception:
            session.close()
            return False

        for raw_user in raw_users:
            raw_dict = raw_user.__dict__
            del raw_dict['_sa_instance_state']
            raw_users_dict.append(raw_dict)

        session.close()
        return raw_users_dict

    def promote_user(self, *, id, user_type):  # DONE
        session = self.db.create_session()

        try:
            session.query(User).filter(User.id == id).update({'user_type': f'{user_type}'})
        except Exception:
            session.close()
            return False

        session.commit()
        session.close()

    def delete_user(self, *, id):  # DONE - (Works, but prints error?)
        session = self.db.create_session()
        session.query(User).filter(User.id == id).delete()
        session.commit()
        session.close()
