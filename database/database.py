import logging
import os

import psycopg
from psycopg.errors import DuplicateTable

log = logging.getLogger(__name__)
schema_file = os.path.dirname(__file__) + "/schema.sql"


class Database:
    connectionUrl = None

    def __init__(self):
        if self.connectionUrl is None:
            raise ValueError("Database connection URL not specified!")
        self._conn = psycopg.connect(Database.connectionUrl)
        self._cursor = self._conn.cursor()
        self.connection.autocommit = True
        self.__initSchema()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()

    def commit(self):
        self.connection.commit()

    @property
    def cursor(self):
        return self._cursor

    @property
    def connection(self):
        return self._conn

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def isAlive(self):
        return self.query("SELECT 1")

    def execute(self, sql, params=None):
        return self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def __initSchema(self):
        try:
            self.execute(open(schema_file, "r").read())
        except DuplicateTable:
            log.info("Database was already initialized")
