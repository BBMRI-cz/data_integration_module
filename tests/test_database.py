import unittest

from testcontainers.postgres import PostgresContainer

from database.database import Database


class DatabaseTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls._postgresContainer = PostgresContainer("postgres:14", dbname="biobank")
        cls._postgresContainer.start()
        url = cls._postgresContainer.get_connection_url().split("+")[1].replace("psycopg2", "postgresql")
        cls._db = Database(url)

    def test_ConnectionIsAlive(self):
        self.assertTrue(self._db.isAlive())

    def test_PostgresVersion(self):
        version = self._db.query("select version()")
        self.assertIn("14", version[0][0])

    def test_InitDBSchema(self):
        self._db.initSchema()
        result = self._db.query("SELECT to_regclass('biobank_record')")
        self.assertEquals(result[0][0], "biobank_record")

    @classmethod
    def tearDownClass(cls) -> None:
        cls._db.close()
        cls._postgresContainer.stop()
