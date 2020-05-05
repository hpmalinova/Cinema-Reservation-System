import hashlib
from .validation import validate_email, validate_password


class UserModel:
    def __init__(self, *, user_id, email, password, user_type):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.user_type = user_type

    @staticmethod
    def validate(email, password):
        validate_email(email)
        validate_password(password)

    @staticmethod
    def hash_password(password):  # TODO: FIX Hashing function!
        for i in range(100000):
            password = hashlib.sha256(password.encode()).hexdigest()
        return password
