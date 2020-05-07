SELECT_ALL_MOVIES = '''
    SELECT *
        FROM movies
    ORDER BY rating DESC
'''

CREATE_QUERY = '''
    INSERT INTO movies (title, year, rating)
        VALUES (?, ?, ?);
'''

GET_MOVIE_ID = '''
    SELECT id
        FROM movies
        WHERE title=? and year=?
'''

GET_MOVIE_BY_ID = '''
    SELECT *
        FROM movies
        WHERE id=?;
'''

DELETE_MOVIE_BY_ID = '''
    DELETE FROM movies
        WHERE id=?
'''

GET_TITLE_BY_ID = '''
    SELECT title
        FROM movies
        WHERE id=?
'''
