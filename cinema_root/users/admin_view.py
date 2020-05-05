# User
# delete user
# show all users
# show all clients
# change type ? (client-->admin)


# Movie
# add
# delete
# update title/ year
# show all by rating)
# update rating (id)

# Projections
# add
# delete
# update/time/type

class AdminView:
    def __init__(self, user):
        self.user = user
        self.welcome()

    def welcome(self):
        print(f'Welcome to HackCinema, {self.user.name}')
