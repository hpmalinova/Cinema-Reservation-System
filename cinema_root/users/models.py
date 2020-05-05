import hashlib
from .validation import validate_email, validate_password


class UserModel:
    def __init__(self, *, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def validate(email, password):
        validate_email(email)
        validate_password(password)

    @staticmethod
    def hash_password(password):  # TODO: FIX Hashing function!
        for i in range(100000):
            password = hashlib.sha256(password.encode()).hexdigest()
        return password

