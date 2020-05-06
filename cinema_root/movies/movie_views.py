from .controllers import MovieController


class MovieViews:
    def __init__(self):
        self.controller = MovieController()

    def show_all_movies(self):
        movies = self.controller.show_all_movies()
        for movie in movies:
            print(f'''
    ------------------
    ID: {movie.movie_id}
    Title: {movie.title}
    Year: {movie.year}
    Rating: {movie.rating}
    ------------------''')

    @staticmethod
    def get_input(msg):
        var = input(msg)
        while not var:
            var = input(msg)
        return var


class AdminMovieView(MovieViews):
    def __init__(self):
        super().__init__()

    def add_movie(self):
        title = self.get_input('Enter title: ')
        year = self.get_input('Enter year: ')
        rating = self.get_input('Enter rating: ')

        self.controller.add_movie(title, year, rating)

    def delete_movie(self):
        movie_id = self.get_input('Enter id of the movie you want to delete: ')
        self.controller.delete_movie(movie_id)
