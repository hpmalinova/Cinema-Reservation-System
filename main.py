from cinema_root.db import create_tables
from cinema_root.db_schema import init_db
from cinema_root.index_view import welcome
import sys


class Application:
    @classmethod
    def build(self):
        create_tables()
        init_db()
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
