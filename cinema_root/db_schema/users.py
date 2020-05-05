# TODO: Hash the passwords
CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(50) NOT NULL,
        user_type VARCHAR(10) NOT NULL CHECK(user_type = 'Admin' or user_type = 'Client')
    );
'''
