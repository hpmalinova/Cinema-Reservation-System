from .movies_gateway import MovieGateway


class MovieController:
    def __init__(self):
        self.gateway = MovieGateway()

    def show_all_movies(self):
        return self.gateway.show_all_movies()

    def add_movie(self, title, year, rating):
        return self.gateway.add_movie(title, year, rating)

    def delete_movie(self, id):
        return self.gateway.delete_movie(id)
