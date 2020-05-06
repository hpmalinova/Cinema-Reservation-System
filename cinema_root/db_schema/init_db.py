INIT_USERS = '''
    INSERT INTO users(email, password, user_type)
        VALUES
        ("admin_hackcinema@gmail.com", "17ecee6d6b011925124c7d893d4e88e15a1d2377ebe41132d07bfdceadd273fa", "Admin"),
        ("ivan_petrov@abv.bg", "1b662a97c8895e12a695f08f33442d27e9fe63f62dc4df908439b0a2a789099c", "Client"),
        ("georgi_toshev@yahoo.com", "5f2fb4cbed8d6790efc9ce9f583d6f571e36f73497ed7d0069b2297ab382e019", "Client"),
        ("pesho.petrov@abv.bg", "abba356287d6ce18942a0136b10c6651f47a45a1115a2cbc47e434d9b0475fdc", "Client"),
        ("ludmil.dimitrov@abv.bg", "cabe072d04cfb72f18a9bab9432d41184967dfc3fac386927551a9fd79d7c92b", "Client"),
        ("stefan.n@abv.bg", "5bef7721b8fbcab3f5aabb046e32e2abe37f2851a5b069205ade878f99bbdee8", "Client")
'''

INIT_MOVIES = '''
    INSERT INTO movies(title, year, rating)
        VALUES("Jojo Rabbit", 2019, 7.9),
        ("Black Widow", 2020, 0.0),
        ("Harley Quinn: Birds of Prey", 2020, 6.2)
'''

INIT_PROJECTIONS = '''
    INSERT INTO projections(movie_id, p_type, p_date, p_time)
        VALUES(1, "3D", "2020-05-15", "19:10"),
        (1, "4DX", "2020-05-15", "21:00"),
        (2, "4DX", "2020-06-15", "18:00"),
        (1, "3D", "2020-06-15", "20:30")
'''
