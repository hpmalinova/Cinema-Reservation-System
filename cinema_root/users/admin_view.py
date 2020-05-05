class AdminView:
    def __init__(self, user):
        self.user = user
        self.welcome()

    def welcome(self):
        print(f'Welcome to HackCinema, {self.user.name}')
