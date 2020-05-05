from cinema_root.db import Database
from cinema_root.db_schema import *
from cinema_root.index_view import welcome

import sys


class Application:
    @classmethod
    def build(self):
        db = Database()
        db.cursor.execute(CREATE_USERS)
        # TODO: Build rest of the tables
        # TODO: Seed with inistial data - consider using another command for this

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
