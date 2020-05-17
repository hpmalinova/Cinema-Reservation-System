from cinema_root.db import session_scope
from cinema_root.db_schema import User


class UserGateway:
    def add_user(self, *, email, hashed_password):
        with session_scope() as session:
            user = User(email=email, password=hashed_password, user_type="Client")
            session.add(user)

            raw_user = session.query(User)\
                              .filter(User.email == email)\
                              .one()

            raw_dict = raw_user.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict

    def login(self, *, email, hashed_password):
        with session_scope() as session:
            raw_user = session.query(User)\
                              .filter(User.email == email)\
                              .first()

            if raw_user and hashed_password == raw_user.__dict__['password']:
                raw_dict = raw_user.__dict__
                del raw_dict['_sa_instance_state']
                return raw_dict

    def get_user(self, *, user_id):
        with session_scope() as session:
            raw_user = session.query(User)\
                              .filter(User.user_id == user_id)\
                              .first()
            if raw_user:
                raw_dict = raw_user.__dict__
                del raw_dict['_sa_instance_state']

                return raw_dict

    def get_all_users(self):
        with session_scope() as session:
            raw_users_dict = []
            raw_users = session.query(User)

            for raw_user in raw_users:
                raw_dict = raw_user.__dict__
                del raw_dict['_sa_instance_state']
                raw_users_dict.append(raw_dict)

            return raw_users_dict

    def promote_user(self, *, user_id, user_type):
        with session_scope() as session:
            session.query(User)\
                   .filter(User.user_id == user_id)\
                   .update({'user_type': f'{user_type}'})

    def delete_user(self, *, user_id):
        with session_scope() as session:
            session.query(User)\
                   .filter(User.user_id == user_id)\
                   .delete()
