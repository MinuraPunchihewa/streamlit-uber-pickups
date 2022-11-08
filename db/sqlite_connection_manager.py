import sqlite3


class SQLiteConnectionManager:

    def __init__(self, db_file):
        """ SQLite database connection context manager """
        self.db_file = db_file

    def __enter__(self):
        """ create a database connection to the SQLite database specified by the db_file
        """
        self.connection = None
        try:
            self.connection = sqlite3.connect(self.db_file)
        except Exception as e:
            print(e)

        return self.connection

    def __exit__(self, type, value, traceback):
        """ Close the open connection to the database """
        self.connection.close()