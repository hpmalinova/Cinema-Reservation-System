SELECT_ALL_USERS = '''
    SELECT *
    FROM users;
'''

CREATE_USER = '''
    INSERT INTO users (email, password, user_type)
        VALUES (?, ?, ?);
'''

GET_USER_ID = '''
    SELECT id
        FROM users
        WHERE email=?;
'''

GET_USER_BY_ID = '''
    SELECT *
        FROM users
        WHERE id=?;
'''

GET_USER_BY_EMAIL = '''
    SELECT *
        FROM users
        WHERE email=?;
'''

GET_CLIENT_BY_ID = '''
    SELECT *
        FROM users
        WHERE id =? and user_type='Client';
'''

MAKE_ADMIN_BY_ID = '''
    UPDATE users
        SET user_type=?
        WHERE id=?;
'''

DELETE_USER_BY_ID = '''
    DELETE FROM users
        WHERE id=?;
'''
