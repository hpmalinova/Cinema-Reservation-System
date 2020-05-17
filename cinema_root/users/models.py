from .validation import validate_email, validate_password
from .users_gateway import UserGateway

import hashlib


class UserModel:
    gateway = UserGateway()

    def __init__(self, *, id, email, password, user_type):
        self.id = id
        self.email = email
        self.password = password
        self.user_type = user_type

    @classmethod
    def validate(cls, email, password):
        validate_email(email)
        validate_password(password)

    @classmethod
    def hash_password(cls, password):  # TODO: FIX Hashing function!
        for i in range(100000):
            password = hashlib.sha256(password.encode()).hexdigest()
        return password

    @classmethod
    def add_user(cls, *, email, password):
        cls.validate(email, password)
        password = cls.hash_password(password)
        raw_user = cls.gateway.add_user(email=email, hashed_password=password)
        if raw_user is not None:  # TODO nz dali traa ima proverka
            return cls(**raw_user)
        else:
            return False

    @classmethod
    def login(cls, *, email, password):
        password = cls.hash_password(password)
        raw_user = cls.gateway.login(email=email, hashed_password=password)

        if raw_user is not None:
            return cls(**raw_user)
        else:
            return False

    @classmethod
    def get_all_users(cls):
        raw_users = cls.gateway.get_all_users()

        all_users = []
        for raw_user in raw_users:
            user_model = cls(**raw_user)
            all_users.append(user_model)

        return all_users

    @classmethod
    def get_user(cls, *, id):
        raw_user = cls.gateway.get_user(id=id)
        if raw_user is not None:
            return cls(**raw_user)

    @classmethod
    def promote_user(cls, *, id, user_type):
        cls.gateway.promote_user(id=id, user_type=user_type)

    @classmethod
    def delete_user(cls, *, id):
        cls.gateway.delete_user(id=id)
