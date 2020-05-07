SELECT_ALL_PROJECTIONS = '''
    SELECT *
        FROM projections
'''

CREATE_PROJECTION = '''
    INSERT INTO projections (movie_id, p_type, p_date, p_time)
        VALUES (?, ?, ?, ?);
'''

GET_PROJECTION_ID = '''
    SELECT p_id
        FROM projections
        WHERE movie_id=? and p_type=?
            and p_date=? and p_time=?;
'''
DELETE_PROJECTION_BY_ID = '''
    DELETE FROM projections
        WHERE p_id=?;
'''

GET_PROJECTION_BY_ID = '''
    SELECT p_id
        FROM projections
        WHERE p_id=?;
'''

UPDATE_PROJECTION = '''
    UPDATE projections
        SET ?=?
        WHERE p_id=?;
'''

GET_PROJECTION_BY_MOVIE_ID = '''
    SELECT *
        FROM projections
        WHERE movie_id=?;
'''
