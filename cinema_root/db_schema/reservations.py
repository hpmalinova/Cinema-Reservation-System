CREATE_RESERVATIONS = '''
    CREATE TABLE IF NOT EXISTS reservations(
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        projection_id INTEGER NOT NULL,
        row INTEGER NOT NULL CHECK(row BETWEEN 1 and 10),
        col INTEGER NOT NULL CHECK(col BETWEEN 1 and 10),
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY(projection_id) REFERENCES projections(p_id) ON DELETE CASCADE
    );
'''
