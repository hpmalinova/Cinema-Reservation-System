class UserModel:
    def __init__(self, *, id, email, password, user_type):
        self.id = id
        self.email = email
        self.password = password
        self.user_type = user_type

    @staticmethod
    def validate(email, password):
        # TODO: Implement a validation -> Raise an error
        pass

    def hash_password(password):
        hashed_password = ''
        return hashed_password

