SELECT_ALL_RESERVATIONS = '''
    SELECT *
        FROM reservations
'''

SELECT_MY_RESERVATIONS = '''
    SELECT *
        FROM reservations
        WHERE user_id=?
'''

CREATE_QUERY = '''
    INSERT INTO reservations(user_id, projection_id, row, col)
        VALUES(?, ?, ?, ?);
'''

GET_RESERVATION_BY_PROJ_ID_ROW_COL = '''
    SELECT *
        FROM reservations
        WHERE projection_id=? AND row=? AND col=?
'''

GET_RESERVATION_BY_USER_ID_PROJ_ID_ROW_COL = '''
    SELECT *
        FROM reservations
        WHERE user_id=? AND projection_id=? AND row=? AND col=?
'''

GET_RESERVATION_BY_ID = '''
    SELECT *
        FROM reservations
        WHERE id=?
'''

GET_RESERVATIONS_BY_PROJ_ID = '''
    SELECT *
        FROM reservations
        WHERE projection_id=?
'''

DELETE_RESERVATION_BY_ID_USER_ID = '''
    DELETE FROM reservations
        WHERE id=? AND user_id=?
'''
