CREATE_PROJECTIONS = '''
    CREATE TABLE IF NOT EXISTS projections(
        id INTEGER PRIMARY KEY,
        movie_id INTEGER NOT NULL,
        type VARCHAR(3) NOT NULL,
        p_date VARCHAR(10) NOT NULL,
        p_time VARCHAR(5) NOT NULL,
        UNIQUE(p_date, p_time),
        FOREIGN KEY(movie_id) REFERENCES movies(id) ON DELETE CASCADE
    );
'''