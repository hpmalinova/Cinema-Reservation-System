from cinema_root.db import Database
from cinema_root.db_schema import *
from cinema_root.index_view import welcome

import sys


class Application:
    @classmethod
    def build(self):
        db = Database()
        # db.cursor.execute(CREATE_USERS)
        # db.cursor.execute(CREATE_MOVIES)
        # db.cursor.execute(CREATE_PROJECTIONS)
        # db.cursor.execute(CREATE_RESERVATIONS)

        # db.cursor.execute(INIT_USERS)
        # db.cursor.execute(INIT_MOVIES)
        # db.cursor.execute(INIT_PROJECTIONS)

        db.connection.commit()
        db.connection.close()

        print('Done.')

    @classmethod
    def start(self):
        welcome()


if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
