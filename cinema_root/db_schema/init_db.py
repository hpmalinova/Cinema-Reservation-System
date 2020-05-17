from .users import User
from .movies import Movie
from .projections import Projection
from cinema_root.db import session_scope


def init_db():
    with session_scope() as session:
        session.add_all([
            User(
                email="admin_hackcinema@gmail.com",
                password="17ecee6d6b011925124c7d893d4e88e15a1d2377ebe41132d07bfdceadd273fa",
                user_type="Admin"
            ),
            User(
                email="ivan_petrov@abv.bg",
                password="1b662a97c8895e12a695f08f33442d27e9fe63f62dc4df908439b0a2a789099c",
                user_type="Client"
            ),
            User(
                email="georgi_toshev@yahoo.com",
                password="5f2fb4cbed8d6790efc9ce9f583d6f571e36f73497ed7d0069b2297ab382e019",
                user_type="Client"
            ),
            User(
                email="pesho.petrov@abv.bg",
                password="abba356287d6ce18942a0136b10c6651f47a45a1115a2cbc47e434d9b0475fdc",
                user_type="Client"
            ),
            User(
                email="ludmil.dimitrov@abv.bg",
                password="cabe072d04cfb72f18a9bab9432d41184967dfc3fac386927551a9fd79d7c92b",
                user_type="Client"
            ),
            User(
                email="stefan.n@abv.bg",
                password="5bef7721b8fbcab3f5aabb046e32e2abe37f2851a5b069205ade878f99bbdee8",
                user_type="Client"
            ),
            Movie(
                title="Jojo Rabbit",
                movie_year=2019,
                rating=7.9
            ),
            Movie(
                title="Black Widow",
                movie_year=2020,
                rating=0.0
            ),
            Movie(
                title="Harley Quinn: Birds of Prey",
                movie_year=2020,
                rating=6.2
            ),
            Projection(
                movie_id=1,
                projection_type="3D",
                projection_date="2020-05-15",
                projection_time="19:10"
            ),
            Projection(
                movie_id=1,
                projection_type="4DX",
                projection_date="2020-05-15",
                projection_time="21:00"
            ),
            Projection(
                movie_id=2,
                projection_type="4DX",
                projection_date="2020-06-15",
                projection_time="18:00"
            ),
            Projection(
                movie_id=1,
                projection_type="3D",
                projection_date="2020-06-15",
                projection_time="20:30"
            )
        ])
